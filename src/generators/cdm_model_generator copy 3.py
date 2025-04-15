#!/usr/bin/env python3
"""
ISDA CDM 6.4 Pydantic Model Generator

This script generates Pydantic models from ISDA CDM JSON schemas.
It creates a hierarchy of Python classes representing the CDM data model.
"""
import os
import sys
import logging
import json
import re
from pathlib import Path
from typing import Dict, List, Any, Set, Tuple, Optional, ForwardRef, TYPE_CHECKING
from dataclasses import dataclass, field
import shutil
from collections import defaultdict

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Constants
SCHEMA_DIR = Path("specifications/cdm_json")
OUTPUT_DIR = Path("src/models/cdm/generated")
FORWARD_REF_SET = set()  # Track classes that need forward references

# Type mapping from JSON Schema to Python
JSON_TYPE_MAP = {
    "string": "str",
    "integer": "int",
    "number": "float",
    "boolean": "bool",
    "array": "List",
    "object": "Dict",
    "null": "None",
    "any": "Any"
}

@dataclass
class CdmProperty:
    """Class for storing CDM property information."""
    name: str
    type_name: str
    description: str = ""
    required: bool = False
    is_array: bool = False
    ref: str = None
    items_ref: str = None
    enum_values: List[str] = field(default_factory=list)

@dataclass
class CdmSchema:
    """Class for storing CDM schema information."""
    name: str
    title: str = ""
    type: str = "object"
    description: str = ""
    properties: Dict[str, CdmProperty] = field(default_factory=dict)
    required: List[str] = field(default_factory=list)
    ref: str = None
    extends: str = None
    
def camel_to_snake(name):
    """Convert CamelCase to snake_case."""
    name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', name).lower()

def snake_to_camel(name):
    """Convert snake_case to CamelCase."""
    return ''.join(word.title() for word in name.split('_'))

def extract_class_name_from_ref(ref: str) -> str:
    """Extract class name from JSON Schema reference."""
    if not ref:
        return None
    
    # Remove file extension and path
    class_name = ref.replace(".schema.json", "")
    if "/" in class_name:
        class_name = class_name.split("/")[-1]
    
    # Extract the actual type name from patterns like cdm-product-template-Product
    parts = class_name.split("-")
    if len(parts) > 1:
        # Take the last part as the class name
        class_name = parts[-1]
    
    # Log some examples
    if ref in ["cdm-product-template-Product.schema.json", "cdm-product-template-TradableProduct.schema.json"]:
        logger.debug(f"Extracted class name '{class_name}' from '{ref}'")
    
    return class_name

def get_module_path_from_ref(ref: str) -> List[str]:
    """Convert a JSON Schema reference to a Python module path."""
    if not ref:
        return []
    
    # Remove file extension
    path = ref.replace(".schema.json", "")
    
    # Extract parts from pattern like cdm-product-template-Product
    parts = path.split("-")
    
    if len(parts) < 2:
        return []
    
    # Handle special cases
    if "rosetta" in parts:
        # Handle rosetta models
        idx = parts.index("rosetta")
        return parts[idx:]  # Include rosetta and everything after
    elif "metafields" in parts:
        # Handle metafields
        idx = parts.index("metafields")
        return parts[1:idx+1]  # Include everything up to and including metafields
    else:
        # Normal case - skip cdm prefix and class name
        return parts[1:-1]

def create_output_directories():
    """Create the necessary output directories."""
    OUTPUT_DIR.mkdir(exist_ok=True, parents=True)
    (OUTPUT_DIR / "base").mkdir(exist_ok=True)
    (OUTPUT_DIR / "metafields").mkdir(exist_ok=True)
    
    # Create directories for modules found in the schema
    for schema_file in SCHEMA_DIR.glob("*.schema.json"):
        parts = schema_file.stem.split("-")
        if len(parts) > 2:
            # Skip the first part (cdm) and the last part (class name)
            modules = parts[1:-1]
            
            # Handle metafields as a special case
            if "metafields" in modules:
                continue
            
            # Create directory structure
            current_dir = OUTPUT_DIR
            for module in modules:
                current_dir = current_dir / module
                current_dir.mkdir(exist_ok=True)

def parse_json_schemas() -> Dict[str, CdmSchema]:
    """Parse all CDM JSON schema files.
    
    Returns:
        Dictionary mapping schema name to CdmSchema object
    """
    logger.info(f"Parsing CDM JSON schemas from {SCHEMA_DIR}")
    schemas = {}
    
    schema_files = list(SCHEMA_DIR.glob("*.schema.json"))
    if not schema_files:
        logger.error(f"No schema files found in {SCHEMA_DIR}")
        sys.exit(1)
    
    logger.info(f"Found {len(schema_files)} schema files")
    
    for schema_file in schema_files:
        try:
            with open(schema_file, 'r') as f:
                json_schema = json.load(f)
            
            # Use the full file stem as the schema name (without .schema.json extension)
            schema_name = schema_file.stem
            if schema_name.endswith(".schema"):
                schema_name = schema_name[:-7]  # Remove .schema suffix
                
            class_name = extract_class_name_from_ref(schema_name)
            
            # Create schema object
            schema = CdmSchema(
                name=schema_name,
                title=json_schema.get("title", class_name),
                type=json_schema.get("type", "object"),
                description=json_schema.get("description", "")
            )
            
            # Process properties
            if "properties" in json_schema:
                for prop_name, prop_def in json_schema["properties"].items():
                    property = CdmProperty(
                        name=prop_name,
                        type_name=prop_def.get("type", "object"),
                        description=prop_def.get("description", ""),
                        required=prop_name in json_schema.get("required", [])
                    )
                    
                    # Handle reference - store the full reference path including file extension
                    if "$ref" in prop_def:
                        # Store the reference with or without file extension
                        ref = prop_def["$ref"]
                        if not ref.endswith(".schema.json"):
                            ref = ref + ".schema.json"
                        property.ref = ref
                    
                    # Handle array types
                    if property.type_name == "array" and "items" in prop_def:
                        property.is_array = True
                        if "$ref" in prop_def["items"]:
                            # Store the reference with or without file extension
                            items_ref = prop_def["items"]["$ref"]
                            if not items_ref.endswith(".schema.json"):
                                items_ref = items_ref + ".schema.json"
                            property.items_ref = items_ref
                    
                    # Handle enums
                    if "enum" in prop_def:
                        property.enum_values = prop_def["enum"]
                    
                    schema.properties[prop_name] = property
            
            # Process required fields
            if "required" in json_schema:
                schema.required = json_schema["required"]
            
            # Add to schemas dictionary
            schemas[schema_name] = schema
            
        except (json.JSONDecodeError, KeyError) as e:
            logger.error(f"Error parsing {schema_file}: {str(e)}")
    
    logger.info(f"Parsed {len(schemas)} CDM schemas")
    
    # Check a few specific schemas to ensure they were parsed correctly
    key_schemas = ["cdm-product-template-Product", "cdm-product-template-TradableProduct", "cdm-product-template-TransferableProduct"]
    for schema_name in key_schemas:
        if schema_name in schemas:
            logger.info(f"Found schema {schema_name} with {len(schemas[schema_name].properties)} properties")
            logger.info(f"Schema properties: {list(schemas[schema_name].properties.keys())}")
        else:
            logger.warning(f"Schema {schema_name} not found")

    # Print some example schema paths to debug
    schema_paths = list(schemas.keys())[:5]
    logger.info(f"Sample schema paths: {schema_paths}")
    
    return schemas

def generate_base_classes():
    """Generate base classes for CDM models."""
    base_dir = OUTPUT_DIR / "base"
    base_dir.mkdir(exist_ok=True)
    
    # Generate base.py
    with open(base_dir / "base.py", "w") as f:
        f.write('''"""
Base classes for ISDA CDM models.
"""
from pydantic import BaseModel, Field, ConfigDict
from typing import Dict, Any, Optional, List, ForwardRef, TYPE_CHECKING, Union
from datetime import date, datetime, time

class CdmModelBase(BaseModel):
    """Base class for all CDM models."""
    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        extra='forbid'
    )
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert model to a dictionary."""
        return self.model_dump(exclude_none=True)
    
    def __str__(self) -> str:
        """String representation of the model."""
        fields = []
        for field_name, field_value in self.model_dump().items():
            if field_value is not None:
                fields.append(f"{field_name}={field_value}")
        return f"{self.__class__.__name__}({', '.join(fields)})"

class CdmProductBase(CdmModelBase):
    """Base class for CDM products."""
    pass

class CdmEventBase(CdmModelBase):
    """Base class for CDM events."""
    pass
''')

def determine_object_dependencies(schemas: Dict[str, CdmSchema]) -> Dict[str, Dict[str, str]]:
    """Determine dependencies between schemas and their types.
    
    Returns:
        Dict mapping schema name to dict of dependencies and their types:
        {
            'schema_name': {
                'dep_schema_name': 'type'  # 'direct', 'array', 'enum', 'base'
            }
        }
    """
    dependencies = defaultdict(dict)
    for schema_name, schema in schemas.items():
        # Track base class dependency
        if schema.extends:
            base_schema = schema.extends.replace(".schema.json", "")
            if base_schema in schemas:
                dependencies[schema_name][base_schema] = 'base'
        
        # Track property dependencies
        for prop_name, prop in schema.properties.items():
            if prop.ref:
                ref_schema = prop.ref.replace(".schema.json", "")
                if ref_schema in schemas:
                    if prop.is_array:
                        dependencies[schema_name][ref_schema] = 'array'
                    else:
                        dependencies[schema_name][ref_schema] = 'direct'
            
            # Track enum dependencies
            if prop.enum_values:
                enum_name = f"{schema_name}_{prop_name}Enum"
                if enum_name in schemas:
                    dependencies[schema_name][enum_name] = 'enum'
    
    return dependencies

def find_circular_dependencies(schemas: Dict[str, CdmSchema]) -> Set[Tuple[str, str]]:
    """Find circular dependencies between schemas."""
    dependencies = determine_object_dependencies(schemas)
    circular_deps = set()
    
    def dfs(node: str, path: List[str]):
        if node in path:
            cycle_start = path.index(node)
            cycle = path[cycle_start:]
            for i in range(len(cycle)):
                circular_deps.add((cycle[i], cycle[(i + 1) % len(cycle)]))
            return
        path.append(node)
        for dep in dependencies.get(node, set()):
            dfs(dep, path.copy())
    
    for schema in schemas:
        dfs(schema, [])
    
    return circular_deps

def generate_init_files():
    """Generate __init__.py files for all directories."""
    # Create root __init__.py
    with open(OUTPUT_DIR / "__init__.py", "w") as f:
        f.write('"""ISDA CDM 6.4 generated models."""\n')
    
    # Create __init__.py for each subdirectory
    for directory in OUTPUT_DIR.glob("**"):
        if directory.is_dir():
            init_file = directory / "__init__.py"
            if not init_file.exists():
                with open(init_file, "w") as f:
                    f.write(f'"""ISDA CDM 6.4 {directory.name} models."""\n')

def determine_base_import(module_path: List[str]) -> str:
    """Determine the correct import path for the base class."""
    if not module_path:
        return "from .base.base import CdmModelBase"
    
    # Calculate number of levels up needed
    up_levels = len(module_path)
    return f"from {'.' * (up_levels + 1)}base.base import CdmModelBase"

def determine_cross_import(current_module: List[str], target_module: List[str], class_name: str) -> str:
    """Determine the correct import path for cross-module imports."""
    if not current_module:
        current_module = []
    if not target_module:
        target_module = []
        
    # Convert string paths to lists if needed
    if isinstance(current_module, str):
        current_module = current_module.split('/')
    if isinstance(target_module, str):
        target_module = target_module.split('/')
        
    # Special case for rosetta models
    if target_module and target_module[0] == "rosetta":
        return f"from src.models.cdm.generated.{'.'.join(target_module)} import {class_name}"
        
    # Find common prefix
    common_prefix_length = 0
    for s, t in zip(current_module, target_module):
        if s == t:
            common_prefix_length += 1
        else:
            break
            
    # Calculate relative path components
    up_levels = len(current_module) - common_prefix_length
    remaining_path = target_module[common_prefix_length:]
    
    # Build the import path
    if up_levels == 0 and not remaining_path:
        return f"from . import {class_name}"
        
    rel_path = "." * (up_levels + 1)  # +1 for the current directory
    if remaining_path:
        rel_path += ".".join(remaining_path)
        
    return f"from {rel_path} import {class_name}"

def determine_property_type(prop_name: str, prop: CdmProperty, class_name: str, module_path: List[str], type_checking_imports: set) -> str:
    """Determine the property type and add necessary imports."""
    if prop.ref:
        ref_class = extract_class_name_from_ref(prop.ref)
        ref_module = get_module_path_from_ref(prop.ref)
        
        # Always use string literals for type hints
        prop_type = f'"{ref_class}"'
        
        # Add import to TYPE_CHECKING block
        if ref_module:
            type_checking_imports.add(determine_cross_import(module_path, ref_module, ref_class))
        else:
            type_checking_imports.add(f"from . import {ref_class}")
        
    elif prop.enum_values:
        # Handle enum types
        enum_name = f"{class_name}_{prop_name}Enum"
        prop_type = f'"{enum_name}"'
        type_checking_imports.add(f"from . import {enum_name}")
    else:
        prop_type = JSON_TYPE_MAP.get(prop.type_name, "Any")
    
    # Handle array types and special fields
    if prop.is_array:
        if prop_name == "business_center":
            # Special handling for business_center field
            type_checking_imports.add("from .metafields import FieldWithMetaBusinessCenterEnum")
            prop_type = 'List["FieldWithMetaBusinessCenterEnum"]'
        elif prop.items_ref:
            items_class = extract_class_name_from_ref(prop.items_ref)
            items_module = get_module_path_from_ref(prop.items_ref)
            if items_module:
                type_checking_imports.add(determine_cross_import(module_path, items_module, items_class))
            else:
                type_checking_imports.add(f"from . import {items_class}")
            prop_type = f'List["{items_class}"]'
        else:
            prop_type = f"List[{prop_type}]"
    
    return prop_type

def generate_cdm_models(schemas: Dict[str, CdmSchema], sorted_schema_names: List[str]):
    """Generate Pydantic models for CDM schemas."""
    # Find dependencies and circular dependencies
    dependencies = determine_object_dependencies(schemas)
    circular_deps = find_circular_dependencies(schemas)
    logger.info(f"Found {len(circular_deps)} circular dependencies")
    
    # Group schemas by module
    module_schemas = defaultdict(list)
    for schema_name in sorted_schema_names:
        if schema_name not in schemas:
            logger.warning(f"Schema {schema_name} not found in schemas, skipping")
            continue
        
        module_path = get_module_path_from_ref(schema_name)
        module_schemas[tuple(module_path)].append(schema_name)
    
    logger.info(f"Generating {len(sorted_schema_names)} CDM models")
    
    # Generate models module by module
    for module_path, schema_names in module_schemas.items():
        # Create module directory
        module_dir = OUTPUT_DIR
        for part in module_path:
            module_dir = module_dir / part
            module_dir.mkdir(exist_ok=True, parents=True)
        
        # Generate each model file
        for i, schema_name in enumerate(schema_names):
            schema = schemas[schema_name]
            class_name = extract_class_name_from_ref(schema_name)
            
            if i % 100 == 0 or i == len(sorted_schema_names) - 1:
                logger.info(f"Generated {i+1}/{len(sorted_schema_names)} models - current: {class_name}")
            
            # Determine file path
            file_path = module_dir / f"{camel_to_snake(class_name)}.py"
            
            # Generate imports
            imports = set()
            type_checking_imports = set()
            
            # Always import basic types and TYPE_CHECKING
            imports.add("from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING")
            imports.add("from datetime import date, datetime, time")
            imports.add("from pydantic import Field, model_validator")
            imports.add("from ...base.base import CdmModelBase")
            
            # Generate class
            class_definition = []
            class_docstring = f'"""{schema.description}"""' if schema.description else '""""""'
            
            # Define class header
            class_def = f"class {class_name}(CdmModelBase):"
            class_definition.append(class_def)
            class_definition.append(f"    {class_docstring}")
            
            # Add properties
            for prop_name, prop in schema.properties.items():
                python_prop_name = camel_to_snake(prop_name)
                
                # Determine property type
                prop_type = determine_property_type(prop_name, prop, class_name, module_path, type_checking_imports)
                
                # Add field definition with correct parameter order
                field_def = f'    {python_prop_name}: {prop_type} = Field('
                if prop.required:
                    field_def += "default=..."
                else:
                    field_def += "None"
                field_def += f', description="{prop.description}")'
                class_definition.append(field_def)
            
            # Write file
            with open(file_path, "w") as f:
                # Write imports
                for imp in sorted(imports):
                    f.write(f"{imp}\n")
                f.write("\n")
                
                # Write TYPE_CHECKING imports
                if type_checking_imports:
                    f.write("if TYPE_CHECKING:\n")
                    for imp in sorted(type_checking_imports):
                        f.write(f"    {imp}\n")
                    f.write("\n")
                
                # Write class definition
                f.write("\n".join(class_definition))
                f.write("\n")
        
        # Update __init__.py with proper import ordering
        update_init_file(module_dir, dependencies, schema_names)
    
    logger.info(f"Generated {len(sorted_schema_names)} CDM models")

def update_init_file(directory: Path, dependencies: Dict[str, Dict[str, str]], module_schemas: List[str]):
    """Update the __init__.py file with dependency-aware import ordering."""
    init_file = directory / "__init__.py"
    
    # Get all classes in this directory and their dependencies
    dir_classes = {}  # class_name -> {dep_name: dep_type}
    for schema_name in module_schemas:
        class_name = extract_class_name_from_ref(schema_name)
        dir_classes[class_name] = {
            extract_class_name_from_ref(dep): dep_type
            for dep, dep_type in dependencies.get(schema_name, {}).items()
        }
    
    # Find circular dependencies within this module
    circular_deps = set()
    for cls1, deps1 in dir_classes.items():
        for cls2 in deps1:
            if cls2 in dir_classes and cls1 in dir_classes[cls2]:
                circular_deps.add((cls1, cls2))
    
    # Sort classes based on dependency types and relationships
    sorted_classes = []
    visited = set()
    temp_visited = set()
    
    def visit(cls):
        if cls in sorted_classes:
            return
        if cls in temp_visited:
            # Circular dependency detected, handle with forward reference
            return
        temp_visited.add(cls)
        
        # Visit dependencies in order: base -> enum -> direct -> array
        deps = dir_classes.get(cls, {})
        for dep, dep_type in sorted(deps.items(), key=lambda x: ['base', 'enum', 'direct', 'array'].index(x[1])):
            if dep in dir_classes and (cls, dep) not in circular_deps:
                visit(dep)
        
        temp_visited.remove(cls)
        if cls not in sorted_classes:
            sorted_classes.append(cls)
    
    # First sort enums and simple types
    for cls in dir_classes:
        deps = dir_classes[cls]
        if cls.endswith('Enum') or all(dep_type == 'enum' for dep_type in deps.values()):
            visit(cls)
    
    # Then sort base types
    for cls in dir_classes:
        deps = dir_classes[cls]
        if any(dep_type == 'base' for dep_type in deps.values()):
            visit(cls)
    
    # Then sort direct dependencies
    for cls in dir_classes:
        deps = dir_classes[cls]
        if any(dep_type == 'direct' for dep_type in deps.values()):
            visit(cls)
    
    # Finally sort array dependencies
    for cls in dir_classes:
        deps = dir_classes[cls]
        if any(dep_type == 'array' for dep_type in deps.values()):
            visit(cls)
    
    # Generate init file content
    content = [f'"""ISDA CDM {directory.name} models."""\n']
    content.append("from typing import TYPE_CHECKING\n\n")
    
    # Add TYPE_CHECKING imports first
    content.append("if TYPE_CHECKING:\n")
    for cls in sorted_classes:
        snake_name = camel_to_snake(cls)
        content.append(f"    from .{snake_name} import {cls}\n")
    content.append("\n")
    
    # Import enums first
    for cls in sorted_classes:
        if cls.endswith('Enum') or all(dep_type == 'enum' for dep_type in dir_classes[cls].values()):
            snake_name = camel_to_snake(cls)
            content.append(f"from .{snake_name} import {cls}\n")
    
    # Import base types next
    for cls in sorted_classes:
        if any(dep_type == 'base' for dep_type in dir_classes[cls].values()):
            snake_name = camel_to_snake(cls)
            content.append(f"from .{snake_name} import {cls}\n")
    
    # Import direct dependencies
    for cls in sorted_classes:
        if any(dep_type == 'direct' for dep_type in dir_classes[cls].values()):
            snake_name = camel_to_snake(cls)
            content.append(f"from .{snake_name} import {cls}\n")
    
    # Import array dependencies last
    for cls in sorted_classes:
        if any(dep_type == 'array' for dep_type in dir_classes[cls].values()):
            snake_name = camel_to_snake(cls)
            content.append(f"from .{snake_name} import {cls}\n")
    
    # Add __all__
    content.append("\n__all__ = [\n")
    for cls in sorted_classes:
        content.append(f"    '{cls}',\n")
    content.append("]\n")
    
    # Write the file
    with open(init_file, "w") as f:
        f.writelines(content)

def main():
    """Main function."""
    logger.info("Starting CDM model generation")
    
    # Create output directories
    create_output_directories()
    
    # Generate base classes
    generate_base_classes()
    
    # Parse schemas
    schemas = parse_json_schemas()
    
    # Get all schema names
    all_schemas = list(schemas.keys())
    logger.info(f"Total CDM schemas: {len(all_schemas)}")
    
    # Generate models for all schemas
    if all_schemas:
        generate_cdm_models(schemas, all_schemas)
    else:
        logger.error("No schemas to generate")
    
    # Generate __init__ files
    generate_init_files()
    
    # Manually generate essential models if they don't exist
    essential_models = [
        ("Product", "product/template"),
        ("TransferableProduct", "product/template"),
        ("TradableProduct", "product/template"),
        ("EconomicTerms", "product/template"),
        ("Payout", "product/template"),
    ]
    
    for model_name, model_path in essential_models:
        path = OUTPUT_DIR / model_path / f"{camel_to_snake(model_name)}.py"
        if not path.exists():
            logger.warning(f"Essential model {model_name} not found, manually generating")
            manual_generate_essential_model(model_name, model_path, schemas)
    
    logger.info("CDM model generation completed successfully")

def manual_generate_essential_model(model_name: str, model_path: str, schemas: Dict[str, CdmSchema]):
    """Manually generate essential models if they were missed."""
    # Find schema by class name
    schema_name = None
    for name, schema in schemas.items():
        if name.endswith(model_name):
            schema_name = name
            break
    
    if not schema_name:
        logger.error(f"Could not find schema for {model_name}")
        return
    
    schema = schemas[schema_name]
    
    # Create directory
    dir_path = OUTPUT_DIR / model_path
    dir_path.mkdir(exist_ok=True, parents=True)
    
    # Create file
    file_path = dir_path / f"{camel_to_snake(model_name)}.py"
    
    with open(file_path, "w") as f:
        f.write(f'''"""
{schema.description}
"""
from typing import Dict, List, Optional, Any, Union
from datetime import date, datetime, time
from pydantic import Field

from ...base.base import CdmModelBase

class {model_name}(CdmModelBase):
    """{schema.description}"""
''')
        
        # Add properties
        for prop_name, prop in schema.properties.items():
            python_prop_name = camel_to_snake(prop_name)
            prop_type = "Optional[Any]"
            if prop.is_array:
                prop_type = "Optional[List[Any]]"
            f.write(f'    {python_prop_name}: {prop_type} = Field(None, description="{prop.description}")\n')
    
    # Update __init__.py
    init_path = dir_path / "__init__.py"
    if not init_path.exists():
        with open(init_path, "w") as f:
            f.write(f'''"""ISDA CDM {model_path.replace("/", " ")} models."""
''')
    
    # Add import to __init__.py
    with open(init_path, "r") as f:
        content = f.read()
    
    import_line = f"from .{camel_to_snake(model_name)} import {model_name}"
    if import_line not in content:
        with open(init_path, "w") as f:
            f.write(content)
            f.write(f"\n{import_line}\n")
            if "__all__" in content:
                # Update existing __all__ list
                f.write(f'__all__ += ["{model_name}"]\n')
            else:
                # Create new __all__ list
                f.write(f'\n__all__ = ["{model_name}"]\n')

if __name__ == "__main__":
    main() 