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
from typing import Dict, List, Any, Set, Tuple, Optional, ForwardRef, TYPE_CHECKING, ClassVar
from dataclasses import dataclass, field
import shutil
from collections import defaultdict
import keyword

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
    enum_values: List[str] = field(default_factory=list)
    
def camel_to_snake(name: str) -> str:
    """Convert camelCase to snake_case."""
    name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    name = re.sub('([a-z0-9])([A-Z])', r'\1_\2', name).lower()
    if keyword.iskeyword(name):
        name = f"{name}_"
    return name

def snake_to_camel(snake_str: str) -> str:
    """Convert snake_case to CamelCase."""
    components = snake_str.split('_')
    return ''.join(x.title() for x in components)

def snake_case(s: str) -> str:
    """Convert any string to snake_case."""
    return camel_to_snake(s)

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
    if "metafields" in parts:
        # All metafields go into the metafields module
        return ["metafields"]
    elif "rosetta" in parts:
        # Handle rosetta models
        idx = parts.index("rosetta")
        return parts[idx:]  # Include rosetta and everything after
    elif "Key" in parts:
        # Handle Key class
        return ["rosetta", "model", "lib", "meta", "Key"]
    elif "Reference" in parts:
        # Handle Reference class
        return ["rosetta", "model", "lib", "meta", "Reference"]
    else:
        # Normal case - skip cdm prefix and class name
        return parts[1:-1]

def create_output_directories():
    """Create the necessary output directories."""
    OUTPUT_DIR.mkdir(exist_ok=True, parents=True)
    (OUTPUT_DIR / "base").mkdir(exist_ok=True)
    (OUTPUT_DIR / "metafields").mkdir(exist_ok=True)
    
    # Create rosetta model lib meta directories
    rosetta_path = OUTPUT_DIR / "rosetta" / "model" / "lib" / "meta"
    rosetta_path.mkdir(exist_ok=True, parents=True)
    (rosetta_path / "Key").mkdir(exist_ok=True)
    
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
                description=json_schema.get("description", ""),
                enum_values=json_schema.get('enum', [])
            )
            
            # Process properties
            if "properties" in json_schema:
                for prop_name, prop_def in json_schema["properties"].items():
                    property = CdmProperty(
                        name=prop_name,
                        type_name=prop_def.get("type", "object"),
                        description=prop_def.get("description", ""),
                        required=prop_name in json_schema.get("required", []),
                        enum_values=prop_def.get('enum', [])
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

def generate_init_file(module_path: List[str], module_dir: Path, schemas: Dict[str, CdmSchema]):
    """Generate an __init__.py file for a module."""
    init_path = module_dir / "__init__.py"
    
    # Get all class names defined in this module
    class_names = set()
    for schema_name in schemas.keys():
        class_name = extract_class_name_from_ref(schema_name)
        class_names.add(class_name)
    
    # Generate imports
    imports = []
    type_checking_imports = []
    
    # Add imports for all classes in this module
    for class_name in sorted(class_names):
        module_name = snake_case(class_name)
        import_path = f"src.models.cdm.generated.{'.'.join(module_path)}.{module_name}"
        type_checking_imports.append(f"from {import_path} import {class_name}")
    
    # Generate the file content
    content = [
        '"""ISDA CDM models."""',
        'from typing import TYPE_CHECKING',
        '',
        'if TYPE_CHECKING:',
    ]
    
    # Add type checking imports
    for imp in sorted(type_checking_imports):
        content.append(f'    {imp}')
    content.append('')
    
    # Add regular imports
    for imp in sorted(imports):
        content.append(imp)
    
    # Write the file
    with open(init_path, 'w') as f:
        f.write('\n'.join(content))

def update_init_file(module_dir: Path, dependencies: Dict[str, Set[str]], schema_names: List[str]) -> None:
    """Update the __init__.py file for a module."""
    init_file = module_dir / "__init__.py"
    module_path = str(module_dir).split("src/models/cdm/generated/")[1].split("/")
    
    # Get all class names defined in this module
    class_names = set()
    for schema_name in schema_names:
        class_name = extract_class_name_from_ref(schema_name)
        class_names.add(class_name)
    
    # Generate imports
    imports = []
    type_checking_imports = []
    
    # Add imports for all classes in this module
    for class_name in sorted(class_names):
        module_name = snake_case(class_name)
        import_path = f"src.models.cdm.generated.{'.'.join(module_path)}.{module_name}"
        type_checking_imports.append(f"from {import_path} import {class_name}")
    
    # Generate the file content
    content = [
        '"""ISDA CDM models."""',
        'from typing import TYPE_CHECKING',
        '',
        'if TYPE_CHECKING:',
    ]
    
    # Add type checking imports
    for imp in sorted(type_checking_imports):
        content.append(f'    {imp}')
    content.append('')
    
    # Add regular imports
    for imp in sorted(imports):
        content.append(imp)
    
    # Write the file
    with open(init_file, "w") as f:
        f.write('\n'.join(content))

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
            
            generate_model_file(schema_name, schema, module_path, module_dir, circular_deps)
        
        # Update __init__.py
        update_init_file(module_dir, dependencies, schema_names)
    
    logger.info(f"Generated {len(sorted_schema_names)} CDM models")

def cleanup_generated_files():
    """Remove all previously generated CDM model files."""
    logger.info("Cleaning up previously generated CDM model files")
    
    if OUTPUT_DIR.exists():
        # Remove all .py files in the generated directory and its subdirectories
        for file in OUTPUT_DIR.glob("**/*.py"):
            try:
                file.unlink()
                logger.debug(f"Removed {file}")
            except Exception as e:
                logger.warning(f"Failed to remove {file}: {e}")
        
        # Remove all empty directories
        for dir_path in sorted([d for d in OUTPUT_DIR.glob("**") if d.is_dir()], reverse=True):
            try:
                dir_path.rmdir()  # This will only remove empty directories
                logger.debug(f"Removed empty directory {dir_path}")
            except Exception as e:
                # Directory not empty or other error, just continue
                pass
    
    # Recreate the output directory
    OUTPUT_DIR.mkdir(exist_ok=True, parents=True)
    logger.info("Cleanup completed")

def get_import_path(current_module: List[str], target_module: List[str], class_name: str) -> str:
    """Generate the proper import path for a class.
    
    Args:
        current_module: Current module path components
        target_module: Target module path components
        class_name: Name of the class to import
        
    Returns:
        Import path as string
    """
    # Special cases for well-known types
    if class_name == "Key":
        return "src.models.cdm.generated.rosetta.model.lib.meta.Key.key"
    elif class_name == "Reference":
        return "src.models.cdm.generated.rosetta.model.lib.meta.Reference.reference"
    elif class_name == "MetaFields":
        return "src.models.cdm.generated.metafields.meta_fields"
    elif class_name.startswith("FieldWithMeta"):
        return f"src.models.cdm.generated.metafields.{camel_to_snake(class_name)}"
    
    # Handle metafields
    if "metafields" in target_module:
        return f"src.models.cdm.generated.metafields.{camel_to_snake(class_name)}"
    
    # Handle rosetta models
    if "rosetta" in target_module:
        rosetta_idx = target_module.index("rosetta")
        path_parts = target_module[rosetta_idx:]
        return f"src.models.cdm.generated.{'_'.join(path_parts)}.{camel_to_snake(class_name)}"
    
    # Handle regular modules
    if target_module:
        return f"src.models.cdm.generated.{'.'.join(target_module)}.{camel_to_snake(class_name)}"
    
    # Default case - use current module
    return f"src.models.cdm.generated.{'.'.join(current_module)}.{camel_to_snake(class_name)}"

def determine_property_type(prop_name: str, prop: CdmProperty, class_name: str, module_path: List[str], type_checking_imports: set, regular_imports: set, circular_deps: Set[Tuple[str, str]]) -> str:
    """Determine the Python type annotation for a property.
    
    Args:
        prop_name: Name of the property
        prop: Property definition
        class_name: Name of the containing class
        module_path: Current module path components
        type_checking_imports: Set to track imports needed for type checking
        regular_imports: Set to track regular imports
        circular_deps: Set of known circular dependencies
        
    Returns:
        Type annotation as string
    """
    if prop.enum_values:
        return class_name + snake_to_camel(prop_name) + "Enum"
        
    if prop.ref:
        ref_class = extract_class_name_from_ref(prop.ref)
        ref_module = get_module_path_from_ref(prop.ref)
        
        # Special handling for Key, Reference, and MetaFields
        if ref_class == "Key":
            import_path = "src.models.cdm.generated.rosetta.model.lib.meta.Key.key"
        elif ref_class == "Reference":
            import_path = "src.models.cdm.generated.rosetta.model.lib.meta.Reference.reference"
        elif ref_class == "MetaFields":
            import_path = "src.models.cdm.generated.metafields.meta_fields"
        elif ref_class.startswith("FieldWithMeta"):
            import_path = f"src.models.cdm.generated.metafields.{camel_to_snake(ref_class)}"
        else:
            import_path = get_import_path(module_path, ref_module, ref_class)
        
        # Add imports
        type_checking_imports.add(f'from {import_path} import {ref_class}')
        regular_imports.add(f'from {import_path} import {ref_class}')
        
        # Handle array types
        if prop.is_array:
            if prop_name == "additional_term":
                return f'Optional[List[ForwardRef("FieldWithMetaString")]]'
            elif prop_name == "key":
                return f'Optional[List[ForwardRef("Key")]]'
            return f'List[ForwardRef("{ref_class}")]'
        else:
            return f'ForwardRef("{ref_class}")'
            
    # Handle basic types
    if prop.type_name in JSON_TYPE_MAP:
        base_type = JSON_TYPE_MAP[prop.type_name]
        if prop.is_array:
            if prop.items_ref:
                items_class = extract_class_name_from_ref(prop.items_ref)
                items_module = get_module_path_from_ref(prop.items_ref)
                
                # Special handling for array items
                if items_class == "Key":
                    import_path = "src.models.cdm.generated.rosetta.model.lib.meta.Key.key"
                elif items_class == "Reference":
                    import_path = "src.models.cdm.generated.rosetta.model.lib.meta.Reference.reference"
                elif items_class == "MetaFields":
                    import_path = "src.models.cdm.generated.metafields.meta_fields"
                elif items_class.startswith("FieldWithMeta"):
                    import_path = f"src.models.cdm.generated.metafields.{camel_to_snake(items_class)}"
                else:
                    import_path = get_import_path(module_path, items_module, items_class)
                
                type_checking_imports.add(f'from {import_path} import {items_class}')
                regular_imports.add(f'from {import_path} import {items_class}')
                return f'List[ForwardRef("{items_class}")]'
            return f'List[{base_type}]'
        return base_type
    
    return 'Any'  # Default to Any for unknown types

def sanitize_enum_value(value: str) -> str:
    """Convert an enum value to a valid Python identifier."""
    # Replace hyphens with underscores
    value = value.replace('-', '_')
    # Replace other invalid characters
    value = ''.join(c if c.isalnum() or c == '_' else '_' for c in value)
    # Ensure it starts with a letter or underscore
    if value[0].isdigit():
        value = '_' + value
    return value

def generate_model_file(schema_name: str, schema: CdmSchema, module_path: List[str], module_dir: Path, circular_deps: Set[Tuple[str, str]]):
    """Generate a single model file."""
    class_name = extract_class_name_from_ref(schema_name)
    file_name = snake_case(class_name) + ".py"
    file_path = module_dir / file_name
    
    type_checking_imports = set()
    regular_imports = set()
    
    # Add standard imports
    imports = [
        'from datetime import date, datetime, time',
        'from pydantic import Field, model_validator',
        'from src.models.cdm.generated.base.base import CdmModelBase',
        'from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar'
    ]
    
    # Generate property definitions
    properties = []
    for prop_name, prop in schema.properties.items():
        python_name = snake_case(prop_name)
        python_type = determine_property_type(prop_name, prop, class_name, module_path, type_checking_imports, regular_imports, circular_deps)
        
        # Generate field definition
        field_args = []
        if not prop.required:
            field_args.append("None")
        if prop.description:
            # Escape quotes in description
            escaped_desc = prop.description.replace('"', '\\"')
            field_args.append(f'description="{escaped_desc}"')
        
        field_def = f'Field({", ".join(field_args)})' if field_args else 'Field()'
        properties.append(f'    {python_name}: {python_type} = {field_def}')
    
    # Generate the file content
    content = imports + ['']
    
    # Add TYPE_CHECKING imports
    if type_checking_imports:
        content.append('if TYPE_CHECKING:')
        for imp in sorted(type_checking_imports):
            content.append(f'    {imp}')
        content.append('')
    
    # Add class definition with docstring
    content.extend([
        f'class {class_name}(CdmModelBase):',
        f'    """{schema.description}"""',
    ])
    
    # Add enum values if this is an enum class
    if schema.enum_values:
        content.append('    # Enum values')
        for value in schema.enum_values:
            sanitized_value = sanitize_enum_value(value)
            content.append(f'    {sanitized_value}: ClassVar[str] = "{value}"')
        content.append('')
    
    content.extend(properties)
    content.append('')
    
    # Add regular imports after class definition
    content.append('# Import after class definition to avoid circular imports')
    for imp in sorted(regular_imports):
        content.append(imp)
    
    # Add model_rebuild call after all imports
    content.append(f'{class_name}.model_rebuild()')
    content.append('')  # Add final newline
    
    # Write the file
    with open(file_path, 'w') as f:
        f.write('\n'.join(content))

class CdmModelGenerator:
    """CDM model generator class."""

    def __init__(self, schema_dir: str, output_dir: str):
        """Initialize CDM model generator."""
        self.schema_dir = schema_dir
        self.output_dir = output_dir
        self.schemas = {}
        self.circular_dependencies = set()
        self.type_checking_imports = set()
        self.regular_imports = set()

    def _is_python_keyword(self, name: str) -> bool:
        """Check if a name is a Python keyword."""
        return keyword.iskeyword(name)

    def _sanitize_property_name(self, name: str) -> str:
        """Sanitize a property name to be valid in Python."""
        if self._is_python_keyword(name):
            return f"{name}_"
        return name

    def _generate_model_fields(self, schema_properties: dict) -> str:
        """Generate model fields from schema properties."""
        fields = []
        for prop_name, prop_details in schema_properties.items():
            sanitized_name = self._sanitize_property_name(prop_name)
            field_type = self._get_field_type(prop_details)
            description = prop_details.get("description", "")
            field_str = f'    {sanitized_name}: {field_type} = Field(None, description="{description}")'
            fields.append(field_str)
        return "\n".join(fields)

    def _get_module_path(self, schema_path: str) -> List[str]:
        """Get module path from schema path."""
        parts = schema_path.replace(".schema.json", "").split("-")
        if parts[0] == "com":
            # Handle com.rosetta.model.metafields namespace
            if "metafields" in parts:
                return ["metafields"]
        if "metafields" in parts:
            # All metafields go into the metafields module
            return ["metafields"]
        return parts[1:]  # Skip the cdm- prefix

    def _get_import_path(self, ref_class: str, target_module: List[str]) -> str:
        """Get import path for a class."""
        # Special handling for MetaFields, Key, Reference, and FieldWithMeta* types
        if ref_class == "MetaFields":
            return "src.models.cdm.generated.metafields.meta_fields"
        if ref_class.startswith("FieldWithMeta"):
            return "src.models.cdm.generated.metafields." + camel_to_snake(ref_class)
        if ref_class in ["Key", "Reference"]:
            return "src.models.cdm.generated.rosetta.model.lib.meta." + ref_class + "." + camel_to_snake(ref_class)
        # Handle other cases
        if "metafields" in target_module:
            return f"src.models.cdm.generated.metafields.{camel_to_snake(ref_class)}"
        return f"src.models.cdm.generated.{'.'.join(target_module)}.{camel_to_snake(ref_class)}"

    def determine_property_type(self, property_schema: Dict[str, Any], property_name: str) -> str:
        if "type" not in property_schema:
            if "$ref" in property_schema:
                ref_type = property_schema["$ref"].split("/")[-1]
                if ref_type == "Key":
                    self.type_checking_imports.add("from src.models.cdm.generated.rosetta.model.lib.meta.Key.key import Key")
                    self.regular_imports.add("from src.models.cdm.generated.rosetta.model.lib.meta.Key.key import Key")
                    return "Key"
                elif ref_type == "Reference":
                    self.type_checking_imports.add("from src.models.cdm.generated.rosetta.model.lib.meta.Reference.reference import Reference")
                    self.regular_imports.add("from src.models.cdm.generated.rosetta.model.lib.meta.Reference.reference import Reference")
                    return "Reference"
                elif ref_type == "MetaFields":
                    self.type_checking_imports.add("from src.models.cdm.generated.metafields.meta_fields import MetaFields")
                    self.regular_imports.add("from src.models.cdm.generated.metafields.meta_fields import MetaFields")
                    return "MetaFields"
                elif ref_type == "FieldWithMetaString":
                    self.type_checking_imports.add("from src.models.cdm.generated.metafields.field_with_meta_string import FieldWithMetaString")
                    self.regular_imports.add("from src.models.cdm.generated.metafields.field_with_meta_string import FieldWithMetaString")
                    return "FieldWithMetaString"
                else:
                    return ref_type
            return "Any"

        if property_schema["type"] == "array":
            if "items" in property_schema:
                item_type = self.determine_property_type(property_schema["items"], property_name)
                if item_type == "Key":
                    self.type_checking_imports.add("from src.models.cdm.generated.rosetta.model.lib.meta.Key.key import Key")
                    self.regular_imports.add("from src.models.cdm.generated.rosetta.model.lib.meta.Key.key import Key")
                    return f"List[Key]"
                elif item_type == "Reference":
                    self.type_checking_imports.add("from src.models.cdm.generated.rosetta.model.lib.meta.Reference.reference import Reference")
                    self.regular_imports.add("from src.models.cdm.generated.rosetta.model.lib.meta.Reference.reference import Reference")
                    return f"List[Reference]"
                elif item_type == "MetaFields":
                    self.type_checking_imports.add("from src.models.cdm.generated.metafields.meta_fields import MetaFields")
                    self.regular_imports.add("from src.models.cdm.generated.metafields.meta_fields import MetaFields")
                    return f"List[MetaFields]"
                elif item_type == "FieldWithMetaString":
                    self.type_checking_imports.add("from src.models.cdm.generated.metafields.field_with_meta_string import FieldWithMetaString")
                    self.regular_imports.add("from src.models.cdm.generated.metafields.field_with_meta_string import FieldWithMetaString")
                    return f"List[FieldWithMetaString]"
                elif item_type == "List":
                    # Handle nested lists for additional_term
                    if property_name == "additional_term":
                        self.type_checking_imports.add("from src.models.cdm.generated.metafields.field_with_meta_string import FieldWithMetaString")
                        self.regular_imports.add("from src.models.cdm.generated.metafields.field_with_meta_string import FieldWithMetaString")
                        return f"List[FieldWithMetaString]"
                    return f"List[List]"
                else:
                    return f"List[{item_type}]"
            return "List"

        if property_schema["type"] in JSON_TYPE_MAP:
            base_type = JSON_TYPE_MAP[property_schema["type"]]
            if property_schema.get("is_array", False):
                return f"List[{base_type}]"
            return base_type

        return "Any"  # Default to Any for unknown types

def main():
    """Main function."""
    logger.info("Starting CDM model generation")
    
    # Clean up old files first
    cleanup_generated_files()
    
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
    
    logger.info("CDM model generation completed successfully")

if __name__ == "__main__":
    main() 