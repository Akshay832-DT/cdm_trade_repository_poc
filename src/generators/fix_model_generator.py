#!/usr/bin/env python3
"""
FIX 4.4 Pydantic Model Generator

This script generates comprehensive Pydantic models for the FIX 4.4 specification.
"""
import os
import sys
import logging
import textwrap
from pathlib import Path
from src.generators.fix_spec_downloader import download_fix_spec, parse_fix_spec, LOCAL_SPEC_PATH
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
import json

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Output directory for generated models
OUTPUT_DIR = Path("src/models/fix/generated")

# FIX type to Python type mapping
FIX_TYPE_MAP = {
    'STRING': 'str',
    'CHAR': 'str',
    'PRICE': 'float',
    'INT': 'int',
    'AMT': 'float',
    'QTY': 'float',
    'CURRENCY': 'str',
    'MULTIPLEVALUESTRING': 'List[str]',
    'EXCHANGE': 'str',
    'UTCTIMESTAMP': 'datetime',
    'BOOLEAN': 'bool',
    'LOCALMKTDATE': 'date',
    'DATA': 'str',
    'FLOAT': 'float',
    'PRICEOFFSET': 'float',
    'MONTHYEAR': 'str',
    'DAYOFMONTH': 'int',
    'UTCDATEONLY': 'date',
    'UTCTIMEONLY': 'time',
    'NUMINGROUP': 'int',
    'PERCENTAGE': 'float',
    'SEQNUM': 'int',
    'LENGTH': 'int',
    'COUNTRY': 'str',
}

def create_output_dirs():
    """Create the necessary output directories."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    os.makedirs(OUTPUT_DIR / "components", exist_ok=True)
    os.makedirs(OUTPUT_DIR / "messages", exist_ok=True)
    os.makedirs(OUTPUT_DIR / "fields", exist_ok=True)

def generate_field_models(fields):
    """
    Generate Pydantic models for FIX fields.
    
    Args:
        fields: Dictionary of field definitions from the FIX specification
    """
    logger.info("Generating field models...")
    
    # Create fields directory if it doesn't exist
    fields_dir = os.path.join(OUTPUT_DIR, 'fields')
    os.makedirs(fields_dir, exist_ok=True)
    
    # Generate common.py with type definitions
    generate_common_field_types(fields_dir)
    
    # Generate __init__.py
    with open(os.path.join(fields_dir, '__init__.py'), 'w') as f:
        f.write("from .base import FIXFieldBase\n")
        f.write("from .types import *\n")
    
    # Generate base.py
    with open(os.path.join(fields_dir, 'base.py'), 'w') as f:
        f.write("""
from pydantic import BaseModel, Field

class FIXFieldBase(BaseModel):
    \"\"\"Base class for FIX fields.\"\"\"
    tag: str
    name: str
    type: str
    description: str = ""
    values: list = []
""")
    
    # Generate types.py
    with open(os.path.join(fields_dir, 'types.py'), 'w') as f:
        f.write("""
from typing import Literal, Union, Optional
from datetime import datetime
from decimal import Decimal

# Define type aliases for FIX field types
FIXString = str
FIXChar = str
FIXPrice = Decimal
FIXInt = int
FIXAmt = Decimal
FIXQty = Decimal
FIXCurrency = str
FIXMultipleValueString = str
FIXExchange = str
FIXMonthYear = str
FIXDayOfMonth = int
FIXBoolean = bool
FIXLocalMktDate = str
FIXData = str
FIXFloat = float
FIXLength = int
FIXNumInGroup = int
FIXPercentage = float
FIXSeqNum = int
FIXUTCTimestamp = datetime
FIXUTCTimeOnly = str
FIXUTCDateOnly = str
FIXCountry = str
FIXTZTimeOnly = str
FIXTZTimestamp = datetime
FIXXMLData = str
FIXLanguage = str
""")
    
    # Generate field models
    for field_name, field_info in fields.items():
        field_tag = field_info['tag']
        field_type = field_info['type']
        field_values = field_info.get('values', {})
        
        # Map FIX types to Python types
        type_mapping = {
            'STRING': 'FIXString',
            'CHAR': 'FIXChar',
            'PRICE': 'FIXPrice',
            'INT': 'FIXInt',
            'AMT': 'FIXAmt',
            'QTY': 'FIXQty',
            'CURRENCY': 'FIXCurrency',
            'MULTIPLEVALUESTRING': 'FIXMultipleValueString',
            'EXCHANGE': 'FIXExchange',
            'MONTHYEAR': 'FIXMonthYear',
            'DAYOFMONTH': 'FIXDayOfMonth',
            'BOOLEAN': 'FIXBoolean',
            'LOCALMKTDATE': 'FIXLocalMktDate',
            'DATA': 'FIXData',
            'FLOAT': 'FIXFloat',
            'LENGTH': 'FIXLength',
            'NUMINGROUP': 'FIXNumInGroup',
            'PERCENTAGE': 'FIXPercentage',
            'SEQNUM': 'FIXSeqNum',
            'UTCTIMESTAMP': 'FIXUTCTimestamp',
            'UTCTIMEONLY': 'FIXUTCTimeOnly',
            'UTCDATEONLY': 'FIXUTCDateOnly',
            'COUNTRY': 'FIXCountry',
            'TZTIMEONLY': 'FIXTZTimeOnly',
            'TZTIMESTAMP': 'FIXTZTimestamp',
            'XMLDATA': 'FIXXMLData',
            'LANGUAGE': 'FIXLanguage'
        }
        
        python_type = type_mapping.get(field_type, 'FIXString')
        
        # Create field model file
        field_file = os.path.join(fields_dir, f"{field_name.lower()}.py")
        with open(field_file, 'w') as f:
            f.write(f"""
from .base import FIXFieldBase
from .types import {python_type}

class {field_name}(FIXFieldBase):
    \"\"\"FIX {field_name} field.\"\"\"
    tag: str = "{field_tag}"
    name: str = "{field_name}"
    type: str = "{field_type}"
    value: {python_type}
""")
            
            # Add enum values if present
            if field_values:
                f.write("\n    # Enum values\n")
                for enum_value, description in field_values.items():
                    f.write(f"    # {enum_value}: {description}\n")

def generate_common_field_types(fields_dir):
    """Generate the common.py file with type definitions used by all components."""
    logger.info("Generating common field types...")
    
    common_py_path = os.path.join(fields_dir, "common.py")
    with open(common_py_path, "w") as f:
        f.write('''"""
Common field types for FIX 4.4 messages.

This module provides common field type definitions used by FIX 4.4 components and messages.
"""
from typing import Optional, Union, List, Dict, Any
from datetime import datetime, date, time
from pydantic import BaseModel, Field

# Define common type aliases
TagNum = str  # FIX tag numbers
NumInGroup = int  # Number of repeated groups
SeqNum = int  # Message sequence number
Length = int  # Length field
Boolean = str  # Y/N boolean
Price = float  # Price field
Qty = float  # Quantity field
Currency = str  # Currency code
Country = str  # Country code
Exchange = str  # Exchange identifier
UTCTimestamp = datetime  # UTC timestamp
UTCDate = date  # UTC date
UTCTimeOnly = time  # UTC time
LocalMktDate = date  # Local market date
Percentage = float  # Percentage
Amt = float  # Monetary amount
MultipleValueString = str  # Multiple value string
''')

def to_camel_case(name):
    """Convert a PascalCase name to camelCase and handle Python keywords."""
    # List of Python keywords that need special handling
    python_keywords = {
        'yield', 'from', 'class', 'def', 'return', 'pass', 'raise', 'break', 'continue',
        'import', 'as', 'global', 'assert', 'if', 'else', 'elif', 'while', 'for', 'try',
        'except', 'finally', 'with', 'lambda', 'or', 'and', 'not', 'is', 'in', 'del'
    }
    
    # Convert to camelCase
    camel_case = name[0].lower() + name[1:] if name else name
    
    # If it's a Python keyword, append 'Value'
    if camel_case.lower() in python_keywords:
        camel_case += 'Value'
    
    return camel_case

def generate_component_models(components, fields, output_dir):
    """Generate Pydantic models for FIX components."""
    logger.info("Generating component models...")
    components_dir = os.path.join(output_dir, "components")
    os.makedirs(components_dir, exist_ok=True)

    # Create __init__.py
    init_path = os.path.join(components_dir, "__init__.py")
    with open(init_path, "w") as f:
        f.write("# FIX 4.4 Component models\n")

    # Track which component files have been written to avoid duplicates
    written_components = set()

    for comp_name, comp_fields in components.items():
        # Skip if we've already written this component file
        if comp_name.lower() in written_components:
            logger.info(f"Skipping duplicate component {comp_name} (already processed)")
            continue

        # Mark this component as written
        written_components.add(comp_name.lower())
        
        # Set to track imported components to avoid duplicates
        imported_components = set()
        
        # Import preamble
        imports = [
            '"""\n',
            f"FIX 4.4 {comp_name} Component\n\n",
            f"This module contains the Pydantic model for the {comp_name} component.\n",
            '"""\n',
            "from datetime import datetime, date, time\n",
            "from typing import List, Optional, Union, Dict, Any, Literal\n",
            "from pydantic import Field, ConfigDict\n",
            "from src.models.fix.generated.fields.common import *\n",
            "from src.models.fix.base import FIXComponentBase\n"
        ]

        # Track the mapping of components to their respective groups
        component_to_group_map = {}
        group_fields = {}
        field_names_in_groups = set()

        # Process fields to identify groups and their components
        for field in comp_fields:
            if field.get('is_group', False):
                group_name = field['name']
                group_fields[group_name] = []
                for group_field in field.get('fields', []):
                    if group_field.get('is_component', False):
                        component_name = group_field['name']
                        component_to_group_map[component_name] = group_name
                    group_fields[group_name].append(group_field)
                    field_names_in_groups.add(group_field['name'].lower())

        # Generate group classes first
        group_classes = []
        for group_name, group_field_list in group_fields.items():
            # Add "Group" suffix to group class names
            class_name = f"{group_name}Group"
            group_class = [
                f"class {class_name}(FIXComponentBase):\n",
                f'    """\n',
                f"    {group_name} group fields\n",
                f'    """\n',
                f"    model_config = ConfigDict(\n",
                f"        populate_by_name=True,\n",
                f"        validate_by_name=True,\n",
                f"        json_encoders={{\n",
                f"            datetime: lambda v: v.isoformat(),\n",
                f"            date: lambda v: v.isoformat(),\n",
                f"            time: lambda v: v.isoformat()\n",
                f"        }}\n",
                f"    )\n",
                f"    \n"
            ]
            
            # Add fields to the group class
            for field in group_field_list:
                field_name = field.get('name', '')
                field_type = field.get('type', 'STRING')
                tag = field.get('tag', '')
                description = field.get('description', '')
                required = field.get('required', False)
                
                if field.get('is_component', False):
                    # Handle component fields
                    if required:
                        group_class.append(f"    {field_name}: {field_name}Component = Field(..., description='{field_name} component')\n")
                    else:
                        group_class.append(f"    {field_name}: Optional[{field_name}Component] = Field(None, description='{field_name} component')\n")
                else:
                    # Handle regular fields
                    python_type = FIX_TYPE_MAP.get(field_type, 'str')
                    if required:
                        group_class.append(f"    {field_name}: {python_type} = Field(..., description='{description}', alias='{tag}')\n")
                    else:
                        group_class.append(f"    {field_name}: Optional[{python_type}] = Field(None, description='{description}', alias='{tag}')\n")
            
            group_class.append("\n\n")
            group_classes.extend(group_class)
        
        # Generate the main component class
        component_class = [
            f"class {comp_name}Component(FIXComponentBase):\n",
            f'    """\n',
            f"    FIX 4.4 {comp_name} Component\n",
            f'    """\n',
            f"    model_config = ConfigDict(\n",
            f"        populate_by_name=True,\n",
            f"        validate_by_name=True,\n",
            f"        json_encoders={{\n",
            f"            datetime: lambda v: v.isoformat(),\n",
            f"            date: lambda v: v.isoformat(),\n",
            f"            time: lambda v: v.isoformat()\n",
            f"        }}\n",
            f"    )\n",
            f"    \n"
        ]
        
        # Add fields to the component class (excluding those in groups)
        for field in comp_fields:
            field_name = field.get('name', '')
            
            # Skip fields that are groups (they'll be added as count and items fields)
            if field.get('is_group', False):
                group_name = field_name
                component_class.append(f"    {group_name}: Optional[int] = Field(None, description='Number of {group_name} entries', alias='{field.get('tag', '')}')\n")
                component_class.append(f"    {group_name}_items: List[{group_name}Group] = Field(default_factory=list)\n")
                continue
                
            # Skip fields that are already in groups to avoid duplication
            if field_name.lower() in field_names_in_groups:
                continue
                
            # Skip component fields that belong to a group
            if field.get('is_component', False) and field_name in component_to_group_map:
                logger.info(f"Skipping component {field_name} in {comp_name} as it belongs to group {component_to_group_map[field_name]}")
                continue
                
            field_type = field.get('type', 'STRING')
            tag = field.get('tag', '')
            description = field.get('description', '')
            required = field.get('required', False)
            
            if field.get('is_component', False):
                # Handle component fields (only if they don't belong to a group)
                if required:
                    component_class.append(f"    {field_name}: {field_name}Component = Field(..., description='{field_name} component')\n")
                else:
                    component_class.append(f"    {field_name}: Optional[{field_name}Component] = Field(None, description='{field_name} component')\n")
            else:
                # Handle regular fields
                python_type = FIX_TYPE_MAP.get(field_type, 'str')
                if required:
                    component_class.append(f"    {field_name}: {python_type} = Field(..., description='{description}', alias='{tag}')\n")
                else:
                    component_class.append(f"    {field_name}: Optional[{python_type}] = Field(None, description='{description}', alias='{tag}')\n")
        
        # Write the component file
        component_file = os.path.join(components_dir, f"{comp_name.lower()}.py")
        with open(component_file, "w") as f:
            f.writelines(imports)
            f.writelines(group_classes)
            f.writelines(component_class)

def generate_message_models(messages: Dict[str, Any], fields: Dict[str, Any], components: Dict[str, Any], output_dir: str) -> None:
    """Generate Pydantic models for FIX messages."""
    logger.info("Generating message models...")
    messages_dir = os.path.join(output_dir, "messages")
    os.makedirs(messages_dir, exist_ok=True)

    # Create __init__.py
    with open(os.path.join(messages_dir, "__init__.py"), "w") as f:
        f.write("# Generated FIX message models\n")

    for message_name, message_info in messages.items():
        # Create message file
        file_path = os.path.join(messages_dir, f"{message_name.lower()}.py")
        with open(file_path, "w") as f:
            # Write imports
            f.write("from typing import Optional, List\n")
            f.write("from datetime import datetime, date, time\n")
            f.write("from pydantic import Field\n")
            f.write("from src.models.fix.base import FIXMessageBase\n")
            
            # Import required components
            imported_components = set()
            for field in message_info.get('fields', []):
                if field.get('is_component', False):
                    component_name = field['name'].replace(" ", "")
                    if component_name not in imported_components:
                        f.write(f"from src.models.fix.generated.components.{component_name.lower()} import {component_name}Component\n")
                        imported_components.add(component_name)
            f.write("\n")

            # Write message class
            f.write(f"class {message_name}(FIXMessageBase):\n")
            f.write('    """FIX message model."""\n\n')

            # Add fields
            for field in message_info.get('fields', []):
                field_name = field['name'].replace(" ", "")
                required = field.get('required', False)

                if field.get('is_component', False):
                    # Handle component fields
                    component_name = field_name
                    python_type = f"{component_name}Component"
                    if not required:
                        python_type = f"Optional[{python_type}]"
                        default_value = "None"
                    else:
                        default_value = "..."  # Pydantic's required marker
                    f.write(f"    {field_name}: {python_type} = Field({default_value}, description='{component_name} component')\n")
                else:
                    # Handle regular fields
                    field_info = fields.get(field_name, {})  # Use original name for lookup
                    fix_type = field_info.get('type', 'STRING')
                    python_type = FIX_TYPE_MAP.get(fix_type, 'str')
                    
                    # Make the field optional if not required
                    if not required:
                        python_type = f"Optional[{python_type}]"
                        default_value = "None"
                    else:
                        default_value = "..."  # Pydantic's required marker
                    
                    # Add field to the model with proper Field alias
                    if 'tag' in field_info:
                        f.write(f"    {field_name}: {python_type} = Field({default_value}, description='{field_info.get('description', '')}', alias='{field_info['tag']}')\n")
                    else:
                        f.write(f"    {field_name}: {python_type} = Field({default_value})\n")

            f.write("\n")

def generate_base_models(output_dir: str) -> None:
    """Generate base models for FIX messages."""
    logger.info("Generating base models...")
    base_dir = os.path.join(output_dir, "base")
    os.makedirs(base_dir, exist_ok=True)

    # Create __init__.py
    with open(os.path.join(base_dir, "__init__.py"), "w") as f:
        f.write("# Generated FIX base models\n")

    # Create base.py
    base_content = '''from datetime import datetime, date, time
from pydantic import BaseModel, ConfigDict

class FIXMessageBase(BaseModel):
    """FIX message base model."""
    model_config = ConfigDict(
        populate_by_name=True,
        validate_by_name=True,
        json_encoders={
            datetime: lambda v: v.isoformat(),
            date: lambda v: v.isoformat(),
            time: lambda v: v.isoformat()
        }
    )
'''
    with open(os.path.join(base_dir, "base.py"), "w") as f:
        f.write(base_content)

def generate_init_file():
    """Generate the __init__.py file for the generated models."""
    logger.info("Generating __init__.py file...")
    
    with open(OUTPUT_DIR / "__init__.py", 'w') as f:
        f.write('''"""
FIX 4.4 Generated Models

This package contains automatically generated Pydantic models for FIX 4.4.
"""
from .base import FIXMessageBase
from .messages import *
from .components import *
''')

def main():
    """Main function to generate FIX 4.4 Pydantic models."""
    # Create output directories
    create_output_dirs()
    
    # Parse FIX specification
    spec_data = parse_fix_spec(str(LOCAL_SPEC_PATH))
    if not spec_data:
        logger.error("Failed to parse FIX 4.4 specification")
        sys.exit(1)
    
    # Generate base models
    generate_base_models(OUTPUT_DIR)
    
    # Generate field models
    generate_field_models(spec_data['fields'])
    
    # Generate component models
    generate_component_models(spec_data['components'], spec_data['fields'], OUTPUT_DIR)
    
    # Generate message models
    generate_message_models(spec_data['messages'], spec_data['fields'], spec_data['components'], OUTPUT_DIR)
    
    # Generate __init__.py
    generate_init_file()
    
    logger.info(f"Successfully generated FIX 4.4 Pydantic models in {OUTPUT_DIR}")

if __name__ == "__main__":
    main() 