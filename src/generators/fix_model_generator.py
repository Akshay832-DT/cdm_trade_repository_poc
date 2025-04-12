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

def generate_component_models(components: Dict[str, Any], fields: Dict[str, Any], output_dir: str) -> None:
    """Generate Pydantic models for FIX components."""
    logger.info("Generating component models...")
    components_dir = os.path.join(output_dir, "components")
    os.makedirs(components_dir, exist_ok=True)

    # Create __init__.py
    with open(os.path.join(components_dir, "__init__.py"), "w") as f:
        f.write("# Generated FIX component models\n")

    for component_name, component_fields in components.items():
        # Skip components without fields
        if not component_fields:
            continue

        # Create component file
        file_path = os.path.join(components_dir, f"{component_name.lower()}.py")
        with open(file_path, "w") as f:
            # Write imports
            f.write("\"\"\"\n")
            f.write(f"FIX 4.4 {component_name} Component\n\n")
            f.write(f"This module contains the Pydantic model for the {component_name} component.\n")
            f.write("\"\"\"\n")
            f.write("from datetime import datetime, date, time\n")
            f.write("from typing import List, Optional, Union, Dict, Any, Literal\n")
            f.write("from pydantic import BaseModel, Field, ConfigDict\n")
            f.write("from src.models.fix.generated.fields.common import *\n")
            f.write("from src.models.fix.base import FIXMessageBase\n")

            # Track imported components
            imported_components = set()
            
            # Identify all components needed for imports
            for field in component_fields:
                # Components in the main component
                if field.get('is_component', False):
                    comp_name = field['name'].replace(" ", "")
                    if comp_name not in imported_components:
                        f.write(f"from src.models.fix.generated.components.{comp_name.lower()} import {comp_name}\n")
                        imported_components.add(comp_name)
                
                # Components in groups
                if field.get('is_group', False):
                    for group_field in field.get('fields', []):
                        if group_field.get('is_component', False):
                            comp_name = group_field['name'].replace(" ", "")
                            if comp_name not in imported_components:
                                f.write(f"from src.models.fix.generated.components.{comp_name.lower()} import {comp_name}\n")
                                imported_components.add(comp_name)
            
            f.write("\n\n")

            # First, generate group classes
            for field in component_fields:
                if field.get('is_group', False):
                    group_name = field['name'].replace(" ", "")
                    f.write(f"class {group_name}(FIXMessageBase):\n")
                    f.write('    """\n')
                    f.write(f'    {group_name} group fields\n')
                    f.write('    """\n')
                    f.write('    model_config = ConfigDict(\n')
                    f.write('        populate_by_name=True,\n')
                    f.write('        validate_by_name=True,\n')
                    f.write('        json_encoders={\n')
                    f.write('            datetime: lambda v: v.isoformat(),\n')
                    f.write('            date: lambda v: v.isoformat(),\n')
                    f.write('            time: lambda v: v.isoformat()\n')
                    f.write('        }\n')
                    f.write('    )\n')
                    f.write('    \n')

                    # Add fields to the group
                    for group_field in field.get('fields', []):
                        field_name = to_camel_case(group_field['name'].replace(" ", ""))
                        required = group_field.get('required', False)

                        if group_field.get('is_component', False):
                            # Handle component fields
                            comp_name = group_field['name'].replace(" ", "")
                            python_type = comp_name
                            if not required:
                                python_type = f"Optional[{python_type}]"
                                default_value = "None"
                            else:
                                default_value = "..."  # Pydantic's required marker
                            f.write(f"    {field_name}: {python_type} = Field({default_value}, description='{comp_name} component')\n")
                        else:
                            # Handle regular fields
                            field_info = fields.get(field_name, {})  # Use original name for lookup
                            if not field_info:
                                # Try the original name if camelCase lookup failed
                                field_info = fields.get(group_field['name'], {})
                            
                            fix_type = field_info.get('type', 'STRING')
                            python_type = FIX_TYPE_MAP.get(fix_type, 'str')
                            
                            # Make the field optional if not required
                            if not required:
                                python_type = f"Optional[{python_type}]"
                                default_value = "None"
                            else:
                                default_value = "..."  # Pydantic's required marker
                            
                            # Add field to the model with proper Field alias
                            tag = None
                            if 'tag' in field_info:
                                tag = field_info['tag']
                            elif 'tag' in group_field:
                                tag = group_field['tag']
                            else:
                                # Look up the tag by field name
                                for f_name, f_info in fields.items():
                                    if f_name.lower() == field_name.lower() or f_name.lower() == group_field['name'].lower():
                                        tag = f_info.get('tag')
                                        break
                            
                            if tag:
                                f.write(f"    {field_name}: {python_type} = Field({default_value}, description='', alias='{tag}')\n")
                            else:
                                f.write(f"    {field_name}: {python_type} = Field({default_value})\n")
                    
                    f.write("\n\n")

            # Write component class
            f.write(f"class {component_name}(FIXMessageBase):\n")
            f.write('    """\n')
            f.write(f'    FIX 4.4 {component_name} Component\n')
            f.write('    """\n')
            f.write('    model_config = ConfigDict(\n')
            f.write('        populate_by_name=True,\n')
            f.write('        validate_by_name=True,\n')
            f.write('        json_encoders={\n')
            f.write('            datetime: lambda v: v.isoformat(),\n')
            f.write('            date: lambda v: v.isoformat(),\n')
            f.write('            time: lambda v: v.isoformat()\n')
            f.write('        }\n')
            f.write('    )\n')
            f.write('    \n')

            # Add non-group fields to main component
            for field in component_fields:
                if not field.get('is_group', False):
                    field_name = to_camel_case(field['name'].replace(" ", ""))
                    required = field.get('required', False)

                    if field.get('is_component', False):
                        # Handle component fields
                        comp_name = field['name'].replace(" ", "")
                        python_type = comp_name
                        if not required:
                            python_type = f"Optional[{python_type}]"
                            default_value = "None"
                        else:
                            default_value = "..."  # Pydantic's required marker
                        f.write(f"    {field_name}: {python_type} = Field({default_value}, description='{comp_name} component')\n")
                    else:
                        # Handle regular fields
                        field_info = fields.get(field_name, {})  # Use original name for lookup
                        if not field_info:
                            # Try the original name if camelCase lookup failed
                            field_info = fields.get(field['name'], {})
                            
                        fix_type = field_info.get('type', 'STRING')
                        python_type = FIX_TYPE_MAP.get(fix_type, 'str')
                        
                        # Make the field optional if not required
                        if not required:
                            python_type = f"Optional[{python_type}]"
                            default_value = "None"
                        else:
                            default_value = "..."  # Pydantic's required marker
                        
                        # Add field to the model with proper Field alias
                        tag = None
                        if 'tag' in field_info:
                            tag = field_info['tag']
                        elif 'tag' in field:
                            tag = field['tag']
                        else:
                            # Look up the tag by field name
                            for f_name, f_info in fields.items():
                                if f_name.lower() == field_name.lower() or f_name.lower() == field['name'].lower():
                                    tag = f_info.get('tag')
                                    break
                        
                        if tag:
                            f.write(f"    {field_name}: {python_type} = Field({default_value}, description='', alias='{tag}')\n")
                        else:
                            f.write(f"    {field_name}: {python_type} = Field({default_value})\n")
                
                # Add group count and list fields
                else:
                    group_name = field['name'].replace(" ", "")
                    
                    # Find the tag for the group count field
                    count_tag = None
                    count_field_name = f"No{group_name}"
                    
                    # First, try to find the count field directly in the fields dictionary
                    for f_name, f_info in fields.items():
                        if f_name == count_field_name:
                            count_tag = f_info.get('tag')
                            break
                    
                    # If not found, try to match by various name formats
                    if not count_tag:
                        for f_name, f_info in fields.items():
                            name_variations = [
                                f"No{group_name}",
                                f"No{field['name'].replace(' ', '')}",
                                f"No{to_camel_case(field['name']).capitalize()}",
                                f"No{to_camel_case(field['name'])}",
                                f"no{field['name'].lower().replace(' ', '')}"
                            ]
                            if f_name in name_variations or f_name.lower() in [n.lower() for n in name_variations]:
                                count_tag = f_info.get('tag')
                                break
                    
                    # Add count field - always required for groups
                    count_field_name = f"no{to_camel_case(group_name)}"
                    if count_tag:
                        f.write(f"    {count_field_name}: Optional[int] = Field(None, description='Number of {group_name} entries', alias='{count_tag}')\n")
                    else:
                        # If we can't find the tag, use a descriptive field name without alias
                        f.write(f"    {count_field_name}: Optional[int] = Field(None, description='Number of {group_name} entries')\n")
                    
                    # Add list field
                    f.write(f"    {count_field_name}_items: List[{group_name}] = Field(default_factory=list)\n")

            f.write("\n")

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
            f.write("from pydantic import Field\n")
            f.write("from src.models.fix.base import FIXMessageBase\n")
            
            # Import required components
            imported_components = set()
            for field in message_info.get('fields', []):
                if field.get('is_component', False):
                    component_name = field['name'].replace(" ", "")
                    if component_name not in imported_components:
                        f.write(f"from src.models.fix.generated.components.{component_name.lower()} import {component_name}\n")
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
                    python_type = component_name
                    if not required:
                        python_type = f"Optional[{python_type}]"
                        default_value = "None"
                    else:
                        default_value = "..."  # Pydantic's required marker
                    f.write(f"    {field_name.lower()}: {python_type} = Field({default_value}, description='{component_name} component')\n")
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
                        f.write(f"    {field_name.lower()}: {python_type} = Field({default_value}, description='{field_info.get('description', '')}', alias='{field_info['tag']}')\n")
                    else:
                        f.write(f"    {field_name.lower()}: {python_type} = Field({default_value})\n")

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