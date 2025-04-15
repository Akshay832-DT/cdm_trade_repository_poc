#!/usr/bin/env python3
"""
FIX 4.4 Pydantic Model Generator

This script generates comprehensive Pydantic models for the FIX 4.4 specification by parsing the FIX44.xml file.
It creates separate Python files for messages, components, and fields while maintaining consistent naming.
"""
import os
import sys
import logging
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Dict, List, Any, Set, Tuple, Optional, ForwardRef, TYPE_CHECKING, Literal
from dataclasses import dataclass
import argparse
import json
import re
from pydantic import model_validator

# Utility functions
def camel_to_snake(name):
    """Convert CamelCase to snake_case."""
    name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', name).lower()

def get_pydantic_type(fix_type):
    """Convert FIX type to Pydantic type."""
    return FIX_TYPE_MAP.get(fix_type, 'Any')

def get_python_type(fix_type: str) -> str:
    """Convert FIX type to Python type."""
    type_map = {
        "INT": "int",
        "NUMINGROUP": "int",
        "SEQNUM": "int",
        "LENGTH": "int",
        "DAYOFMONTH": "int",
        "FLOAT": "float",
        "PRICE": "float",
        "PRICEOFFSET": "float",
        "QTY": "float",
        "AMT": "float",
        "PERCENTAGE": "float",
        "STRING": "str",
        "CHAR": "str",
        "CURRENCY": "str",
        "MULTIPLEVALUESTRING": "str",
        "EXCHANGE": "str",
        "UTCTIMESTAMP": "datetime",
        "UTCTIMEONLY": "time",
        "UTCDATEONLY": "date",
        "LOCALMKTDATE": "date",
        "MONTHYEAR": "str",
        "DATA": "str",
        "BOOLEAN": "bool",
        "COUNTRY": "str",
        "LANGUAGE": "str",
        "XMLDATA": "str",
    }
    return type_map.get(fix_type, "str")

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Constants
SPEC_PATH = Path("specifications/fix/FIX44.xml")
OUTPUT_DIR = Path("src/models/fix/generated")
FIELDS_DIR = OUTPUT_DIR / "fields"
COMPONENTS_DIR = OUTPUT_DIR / "components"
MESSAGES_DIR = OUTPUT_DIR / "messages"

# Define FIX field types mapping to Python types
FIX_TYPE_MAP = {
    'STRING': 'str',
    'CHAR': 'str',
    'PRICE': 'float',
    'INT': 'int',
    'AMT': 'float',
    'QTY': 'float',
    'CURRENCY': 'str',
    'MULTIPLEVALUESTRING': 'List[str]',
    'MULTIPLESTRINGVALUE': 'List[str]',
    'MULTIPLECHARVALUE': 'List[str]',
    'BOOLEAN': 'bool',
    'LOCALMKTDATE': 'date',
    'DATE': 'date',
    'MONTHYEAR': 'str',
    'UTCTIMESTAMP': 'datetime',
    'UTCTIMEONLY': 'time',
    'UTCDATE': 'date',
    'UTCDATEONLY': 'date',
    'NUMINGROUP': 'int',
    'PERCENTAGE': 'float',
    'SEQNUM': 'int',
    'LENGTH': 'int',
    'COUNTRY': 'str',
    'TZTIMEONLY': 'str',
    'TZTIMESTAMP': 'datetime',
    'DATA': 'str',
    'EXCHANGE': 'str',
    'LANGUAGE': 'str',
    'XMLDATA': 'str',
    'DAYOFMONTH': 'int',
    'FLOAT': 'float',
    'PRICEOFFSET': 'float'
}

@dataclass
class FixField:
    """Class for storing FIX field information."""
    number: str  # tag number
    name: str
    type: str
    description: str = ""
    values: Dict[str, str] = None  # enum values and descriptions
    
    def __post_init__(self):
        if self.values is None:
            self.values = {}

@dataclass
class FixComponent:
    """Class for storing FIX component information."""
    name: str
    description: str = ""
    fields: List[Dict[str, Any]] = None
    groups: Dict[str, List[Dict[str, Any]]] = None
    
    def __post_init__(self):
        if self.fields is None:
            self.fields = []
        if self.groups is None:
            self.groups = {}

@dataclass
class FixMessage:
    """Class for storing FIX message information."""
    name: str
    msgtype: str
    category: str
    description: str = ""
    fields: List[Dict[str, Any]] = None
    components: List[str] = None
    
    def __post_init__(self):
        if self.fields is None:
            self.fields = []
        if self.components is None:
            self.components = []

def create_output_directories():
    """Create the necessary output directories."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    os.makedirs(FIELDS_DIR, exist_ok=True)
    os.makedirs(COMPONENTS_DIR, exist_ok=True)
    os.makedirs(MESSAGES_DIR, exist_ok=True)

def parse_fix_spec(xml_path: Path) -> Tuple[Dict[str, Dict], Dict[str, Dict], Dict[str, Dict]]:
    """Parse a FIX specification XML file.
    
    Args:
        xml_path: Path to the FIX specification XML file
        
    Returns:
        Tuple of (fields, components, messages) dictionaries
    """
    logger.info(f"Loading FIX specification from {xml_path}")
    tree = ET.parse(xml_path)
    root = tree.getroot()
    
    # Parse fields
    fields = {}
    for field in root.findall(".//fields/field"):
        field_data = {
            "name": field.attrib["name"],
            "number": field.attrib["number"],
            "type": field.attrib["type"],
            "description": "",
            "enums": {}
        }
        
        # Extract enumerated values
        for value in field.findall("value"):
            field_data["enums"][value.attrib["enum"]] = value.attrib["description"]
            
        fields[field_data["name"]] = field_data
    
    # Parse components
    components = {}
    for component in root.findall(".//components/component"):
        component_data = {
            "name": component.attrib["name"],
            "fields": [],
            "groups": []
        }
        
        # Extract fields
        for field in component.findall("field"):
            field_data = {
                "name": field.attrib["name"],
                "required": field.attrib.get("required", "N") == "Y",
                "number": fields[field.attrib["name"]]["number"],
                "type": fields[field.attrib["name"]]["type"]
            }
            component_data["fields"].append(field_data)
            
        # Extract component references
        for comp_ref in component.findall("component"):
            field_data = {
                "name": comp_ref.attrib["name"],
                "required": comp_ref.attrib.get("required", "N") == "Y",
                "component": comp_ref.attrib["name"]
            }
            component_data["fields"].append(field_data)
            
        # Extract groups
        for group in component.findall("group"):
            group_data = {
                "name": group.attrib["name"],
                "required": group.attrib.get("required", "N") == "Y",
                "number": fields[group.attrib["name"]]["number"],
                "fields": []
            }
            
            # Extract group fields
            for field in group.findall("field"):
                field_data = {
                    "name": field.attrib["name"],
                    "required": field.attrib.get("required", "N") == "Y",
                    "number": fields[field.attrib["name"]]["number"],
                    "type": fields[field.attrib["name"]]["type"]
                }
                group_data["fields"].append(field_data)
                
            # Extract group component references
            for comp_ref in group.findall("component"):
                field_data = {
                    "name": comp_ref.attrib["name"],
                    "required": comp_ref.attrib.get("required", "N") == "Y",
                    "component": comp_ref.attrib["name"]
                }
                group_data["fields"].append(field_data)
                
            component_data["groups"].append(group_data)
            
        components[component_data["name"]] = component_data
    
    # Parse messages
    messages = {}
    for message in root.findall(".//messages/message"):
        message_data = {
            "name": message.attrib["name"],
            "msgtype": message.attrib["msgtype"],
            "msgcat": message.attrib["msgcat"],
            "fields": [],
            "groups": []
        }
        
        # Extract fields
        for field in message.findall("field"):
            field_data = {
                "name": field.attrib["name"],
                "required": field.attrib.get("required", "N") == "Y",
                "number": fields[field.attrib["name"]]["number"],
                "type": fields[field.attrib["name"]]["type"]
            }
            message_data["fields"].append(field_data)
            
        # Extract component references
        for comp_ref in message.findall("component"):
            field_data = {
                "name": comp_ref.attrib["name"],
                "required": comp_ref.attrib.get("required", "N") == "Y",
                "component": comp_ref.attrib["name"]
            }
            message_data["fields"].append(field_data)
            
        # Extract groups
        for group in message.findall("group"):
            group_data = {
                "name": group.attrib["name"],
                "required": group.attrib.get("required", "N") == "Y",
                "number": fields[group.attrib["name"]]["number"],
                "fields": []
            }
            
            # Extract group fields
            for field in group.findall("field"):
                field_data = {
                    "name": field.attrib["name"],
                    "required": field.attrib.get("required", "N") == "Y",
                    "number": fields[field.attrib["name"]]["number"],
                    "type": fields[field.attrib["name"]]["type"]
                }
                group_data["fields"].append(field_data)
                
            # Extract group component references
            for comp_ref in group.findall("component"):
                field_data = {
                    "name": comp_ref.attrib["name"],
                    "required": comp_ref.attrib.get("required", "N") == "Y",
                    "component": comp_ref.attrib["name"]
                }
                group_data["fields"].append(field_data)
                
            message_data["groups"].append(group_data)
            
        messages[message_data["name"]] = message_data
    
    logger.info(f"Loaded {len(fields)} fields, {len(components)} components, and {len(messages)} messages")
    return fields, components, messages

def generate_field_base(fields_dir: Path):
    """Generate base classes for FIX fields."""
    logger.info("Generating field base classes")
    
    # Create base.py with FIXFieldBase class
    base_path = fields_dir / "base.py"
    with open(base_path, "w") as f:
        f.write('''"""
Base classes for FIX field models.
"""
from pydantic import BaseModel, Field, ConfigDict
from typing import Optional, List, Any
from .types import *

# Basic FIX field types
STRING = str
CHAR = str
PRICE = float
INT = int
AMT = float
QTY = float
CURRENCY = str
MULTIPLEVALUESTRING = List[str]
MULTIPLESTRINGVALUE = List[str]
MULTIPLECHARVALUE = List[str]
BOOLEAN = bool
LOCALMKTDATE = date
MONTHYEAR = str
UTCTIMESTAMP = datetime
UTCTIMEONLY = time
UTCDATEONLY = date
NUMINGROUP = int
PERCENTAGE = float
SEQNUM = int
LENGTH = int
DATA = str
COUNTRY = str
EXCHANGE = str
LANGUAGE = str
XMLDATA = str
DAYOFMONTH = int

class FIXFieldBase(BaseModel):
    """Base class for all FIX field models."""
    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True
    )
    
    tag: str
    name: str
    type: str
    description: str = ""
''')

    # Create types.py with type definitions
    types_path = fields_dir / "types.py"
    with open(types_path, "w") as f:
        f.write('''"""
Type definitions for FIX fields.
"""
from typing import List, Optional, Union, Literal
from datetime import datetime, date, time
from decimal import Decimal

# Common FIX field type aliases
FIXString = str
FIXChar = str
FIXPrice = float
FIXInt = int
FIXAmt = float
FIXQty = float
FIXCurrency = str
FIXMultipleValueString = List[str]
FIXMultipleStringValue = List[str]
FIXMultipleCharValue = List[str]
FIXBoolean = bool
FIXLocalMktDate = date
FIXMonthYear = str
FIXUTCTimestamp = datetime
FIXUTCTimeOnly = time
FIXUTCDateOnly = date
FIXNumInGroup = int
FIXPercentage = float
FIXSeqNum = int
FIXLength = int
FIXData = str
FIXCountry = str
FIXExchange = str
FIXLanguage = str
FIXXMLData = str
FIXDayOfMonth = int

# Basic FIX field types
STRING = str
CHAR = str
PRICE = float
INT = int
AMT = float
QTY = float
CURRENCY = str
MULTIPLEVALUESTRING = List[str]
MULTIPLESTRINGVALUE = List[str]
MULTIPLECHARVALUE = List[str]
BOOLEAN = bool
LOCALMKTDATE = date
MONTHYEAR = str
UTCTIMESTAMP = datetime
UTCTIMEONLY = time
UTCDATEONLY = date
NUMINGROUP = int
PERCENTAGE = float
SEQNUM = int
LENGTH = int
DATA = str
COUNTRY = str
EXCHANGE = str
LANGUAGE = str
XMLDATA = str
DAYOFMONTH = int
''')

    # Create __init__.py for fields package
    init_path = fields_dir / "__init__.py"
    with open(init_path, "w") as f:
        f.write('''"""
FIX field models.
"""
from .base import FIXFieldBase
from .types import *
''')

def generate_field_models(fields: Dict[str, FixField], output_dir: Path) -> None:
    """Generate Pydantic models for FIX fields."""
    logger.info("Generating field base classes")
    
    # Create the fields directory
    fields_dir = output_dir / "fields"
    os.makedirs(fields_dir, exist_ok=True)
    
    # Generate field models
    for field_name, field in fields.items():
        # Convert field name to proper file name format
        # Example: BeginString -> beginstring
        file_name = field_name.lower()
        output_path = fields_dir / f"{file_name}.py"
        
        # Get the field type
        field_type = FIX_TYPE_MAP.get(field['type'], "str")
        
        # Write the field model
        with open(output_path, 'w') as f:
            # Write imports
            f.write('"""FIX Field Model"""\n')
            f.write("from typing import Optional, List, Dict, Any, Union, Literal\n")
            f.write("from pydantic import Field, ConfigDict\n")
            f.write("from datetime import datetime, date, time\n")
            f.write("from decimal import Decimal\n")
            f.write("from ..base.base import FIXFieldBase\n\n")
            
            # Write class definition
            class_name = f"{field_name}Field"
            f.write(f"class {class_name}(FIXFieldBase):\n")
            f.write(f'    """FIX {field_name} Field"""\n\n')
            
            # Write model configuration
            f.write("    model_config = ConfigDict(\n")
            f.write("        populate_by_name=True,\n")
            f.write("        validate_assignment=True,\n")
            f.write("        json_encoders={\n")
            f.write("            datetime: lambda v: v.isoformat() if v else None,\n")
            f.write("            date: lambda v: v.isoformat() if v else None,\n")
            f.write("            time: lambda v: v.isoformat() if v else None\n")
            f.write("        }\n")
            f.write("    )\n\n")
            
            # Write field value
            f.write(f"    value: Optional[{field_type}] = Field(None, alias='{field['number']}', description='')\n")
            
            # Write __str__ method
            f.write("\n    def __str__(self) -> str:\n")
            f.write("        return f\"{self.__class__.__name__}(value={self.value})\"\n")
    
    logger.info(f"Generated {len(fields)} field models in {output_dir}")

def generate_base_classes(output_dir: Path) -> None:
    """Generate base classes for FIX models.
    
    Args:
        output_dir: Output directory for generated files
    """
    # Create base directory
    base_dir = output_dir / "base"
    base_dir.mkdir(exist_ok=True)
    
    # Generate base.py
    base_file = base_dir / "base.py"
    with open(base_file, "w") as f:
        f.write('"""Base classes for FIX models."""\n\n')
        f.write("from typing import Dict, Any, Optional\n")
        f.write("from pydantic import BaseModel, Field\n\n")
        
        # Write FIXMessageBase class
        f.write("class FIXMessageBase(BaseModel):\n")
        f.write('    """Base class for FIX messages."""\n\n')
        f.write("    BeginString: str = Field('FIX.4.4', alias='8')\n")
        f.write("    BodyLength: Optional[int] = Field(None, alias='9')\n")
        f.write("    MsgType: str = Field(alias='35')\n")
        f.write("    SenderCompID: Optional[str] = Field(None, alias='49')\n")
        f.write("    TargetCompID: Optional[str] = Field(None, alias='56')\n")
        f.write("    MsgSeqNum: Optional[int] = Field(None, alias='34')\n")
        f.write("    PossDupFlag: Optional[bool] = Field(None, alias='43')\n")
        f.write("    PossResend: Optional[bool] = Field(None, alias='97')\n")
        f.write("    SendingTime: Optional[str] = Field(None, alias='52')\n")
        f.write("    OrigSendingTime: Optional[str] = Field(None, alias='122')\n")
        f.write("    CheckSum: Optional[str] = Field(None, alias='10')\n\n")
        f.write("    def to_dict(self) -> Dict[str, Any]:\n")
        f.write('        """Convert the model to a dictionary.\n\n')
        f.write("        Returns:\n")
        f.write("            Dict[str, Any]: The model as a dictionary\n")
        f.write('        """\n')
        f.write("        return self.model_dump()\n\n")
        f.write("    def __str__(self) -> str:\n")
        f.write('        """Convert the model to a string.\n\n')
        f.write("        Returns:\n")
        f.write("            str: The model as a string\n")
        f.write('        """\n')
        f.write("        fields = []\n")
        f.write("        for field_name, field_value in self.model_dump().items():\n")
        f.write("            if field_value is not None:\n")
        f.write('                fields.append(f"{field_name}={field_value}")\n')
        f.write('        return f"{self.__class__.__name__}({", ".join(fields)})"\n\n')
        
        # Write FIXComponentBase class
        f.write("class FIXComponentBase(BaseModel):\n")
        f.write('    """Base class for FIX components."""\n\n')
        f.write("    def to_dict(self) -> Dict[str, Any]:\n")
        f.write('        """Convert the model to a dictionary.\n\n')
        f.write("        Returns:\n")
        f.write("            Dict[str, Any]: The model as a dictionary\n")
        f.write('        """\n')
        f.write("        return self.model_dump()\n\n")
        f.write("    def __str__(self) -> str:\n")
        f.write('        """Convert the model to a string.\n\n')
        f.write("        Returns:\n")
        f.write("            str: The model as a string\n")
        f.write('        """\n')
        f.write("        fields = []\n")
        f.write("        for field_name, field_value in self.model_dump().items():\n")
        f.write("            if field_value is not None:\n")
        f.write('                fields.append(f"{field_name}={field_value}")\n')
        f.write('        return f"{self.__class__.__name__}({", ".join(fields)})"\n')
    
    # Generate __init__.py
    init_file = base_dir / "__init__.py"
    with open(init_file, "w") as f:
        f.write('"""Base classes for FIX models."""\n\n')
        f.write("from .base import FIXMessageBase, FIXComponentBase\n\n")
        f.write('__all__ = ["FIXMessageBase", "FIXComponentBase"]\n')

def fix_str_method_formatting(content: str) -> str:
    """Fix __str__ method formatting in component files using regex for precision."""
    # Fix group class __str__ method using regex
    group_pattern = r'(return f"{self\.__class__\.__name__}\({", "\.join\(fields\)}\))"(\({", "\.join\(fields\)}\))?'
    content = re.sub(group_pattern, r'\1', content)
    
    # Fix main class __str__ method using regex
    main_pattern = r'(return f"{self\.__class__\.__name__)"(?!\()'
    content = re.sub(main_pattern, r'\1}({", ".join(fields)})"', content)
    
    # Log the changes for debugging
    logger.debug("Fixed str method formatting in component file")
    
    return content

def generate_component_model(component_name: str, component: Dict, fields: Dict, components: Dict, output_dir: Path) -> None:
    """Generate a Pydantic model for a FIX component.
    
    Args:
        component_name: Name of the component
        component: Component definition dictionary
        fields: Dictionary of all fields
        components: Dictionary of all components
        output_dir: Output directory for generated files
    """
    # Convert component name to lowercase for file name (without underscores)
    file_name = component_name.lower()
    file_path = output_dir / "components" / f"{file_name}.py"
    
    # Collect imports
    imports = set()
    imports.add("from typing import Optional, List")
    imports.add("from datetime import date, datetime, time")
    imports.add("from pydantic import Field")
    imports.add("from ..base import FIXComponentBase")
    
    # Process fields and groups
    field_lines = []
    group_classes = []
    
    # First process groups to define them before the main component
    for group in component.get("groups", []):
        group_name = group["name"]
        group_class = f"{group_name}Group"
        
        # Generate group class
        group_field_lines = []
        for field in group["fields"]:
            if isinstance(field, dict) and "component" in field:
                # Nested component in group
                comp_name = field["name"]
                comp_class = f"{comp_name}Component"
                imports.add(f"from .{comp_name.lower()} import {comp_class}")
                if field["required"]:
                    group_field_lines.append(f"    {comp_name}: {comp_class}")
                else:
                    group_field_lines.append(f"    {comp_name}: Optional[{comp_class}] = Field(None, description='{field.get('description', '')}')")
            else:
                # Regular field in group
                field_name = field["name"]
                field_def = fields[field_name]
                field_type = get_python_type(field_def["type"])
                # Only add import for non-builtin types
                if field_type not in ["str", "int", "float", "date", "datetime", "bool", "time"]:
                    imports.add(f"from ..fields.{field_type.lower()} import {field_type}")
                
                if field["required"]:
                    group_field_lines.append(f"    {field_name}: {field_type} = Field(alias='{field_def['number']}', description='{field_def.get('description', '')}')")
                else:
                    group_field_lines.append(f"    {field_name}: Optional[{field_type}] = Field(None, alias='{field_def['number']}', description='{field_def.get('description', '')}')")
        
        # Add group class
        group_classes.append(f"class {group_class}(FIXComponentBase):\n")
        group_classes.append(f'    """FIX Group - {group_name}"""\n')
        group_classes.extend(group_field_lines)
        group_classes.append("\n")
    
    # Process regular fields
    for field in component["fields"]:
        if isinstance(field, dict) and "component" in field:
            # This is a component reference
            comp_name = field["name"]
            comp_class = f"{comp_name}Component"
            imports.add(f"from .{comp_name.lower()} import {comp_class}")
            if field["required"]:
                field_lines.append(f"    {comp_name}: {comp_class}")
            else:
                field_lines.append(f"    {comp_name}: Optional[{comp_class}] = Field(None, description='{field.get('description', '')}')")
        elif isinstance(field, dict) and field.get("is_group", False):
            # Skip group fields here - they're handled in the groups section
            continue
        else:
            # Regular field
            field_name = field["name"]
            field_def = fields[field_name]
            field_type = get_python_type(field_def["type"])
            # Only add import for non-builtin types
            if field_type not in ["str", "int", "float", "date", "datetime", "bool", "time"]:
                imports.add(f"from ..fields.{field_type.lower()} import {field_type}")
            
            if field["required"]:
                field_lines.append(f"    {field_name}: {field_type} = Field(alias='{field_def['number']}', description='{field_def.get('description', '')}')")
            else:
                field_lines.append(f"    {field_name}: Optional[{field_type}] = Field(None, alias='{field_def['number']}', description='{field_def.get('description', '')}')")
    
    # Write the file
    with open(file_path, "w") as f:
        f.write('"""\n')
        f.write(f"FIX Component Model - {component_name}\n")
        f.write('"""\n\n')
        
        # Write imports
        for imp in sorted(imports):
            f.write(f"{imp}\n")
        f.write("\n\n")
        
        # Write group classes first
        f.write("\n".join(group_classes))
        f.write("\n\n")
        
        # Write main component class with __str__ method
        f.write(f"class {component_name}Component(FIXComponentBase):\n")
        f.write(f'    """FIX Component - {component_name}"""\n')
        f.write("\n".join(field_lines))
        f.write("\n\n")

def generate_component_models(components: Dict[str, Dict], output_dir: Path, fields: Dict) -> None:
    """Generate Pydantic models for all FIX components.
    
    Args:
        components: Dictionary of component definitions
        output_dir: Output directory for generated files
        fields: Dictionary of field definitions
    """
    logger.info("Generating component models...")
    
    # Create components directory
    components_dir = output_dir / "components"
    components_dir.mkdir(exist_ok=True)
    
    # Create base directory for component base class
    base_dir = components_dir / "base"
    base_dir.mkdir(exist_ok=True)
    
    # Generate base component class
    base_path = base_dir / "base.py"
    with open(base_path, "w") as f:
        f.write('''"""
Base class for FIX component models.
"""
from pydantic import BaseModel, Field, ConfigDict
from typing import Dict, Any, Optional
from datetime import datetime, date, time

class FIXComponentBase(BaseModel):
    """Base class for all FIX component models."""
    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        json_encoders={
            datetime: lambda v: v.isoformat(),
            date: lambda v: v.isoformat(),
            time: lambda v: v.isoformat()
        }
    )
    
    # Additional fields dictionary
    additional_fields: Dict[str, Any] = Field(default_factory=dict)
    
    def model_dump(self, *args, **kwargs):
        """Convert the component to a dictionary."""
        data = super().model_dump(*args, **kwargs)
        # Process nested components and groups
        for key, value in data.items():
            if hasattr(value, 'model_dump'):
                data[key] = value.model_dump(*args, **kwargs)
            elif isinstance(value, list) and value and hasattr(value[0], 'model_dump'):
                data[key] = [item.model_dump(*args, **kwargs) for item in value]
        return data
        
    def __str__(self):
        return f"{self.__class__.__name__}()"
''')

    # Create base __init__.py
    base_init_path = base_dir / "__init__.py"
    with open(base_init_path, "w") as f:
        f.write('''"""
Base classes for FIX component models.
"""
from .base import FIXComponentBase
''')

    # Generate individual component files
    for component_name, component in components.items():
        file_name = component_name.lower()
        file_path = components_dir / f"{file_name}.py"
        
        # Generate the component model
        generate_component_model(component_name, component, fields, components, output_dir)
        logger.info(f"Generated component model: {file_name}.py")
    
    # Create components __init__.py that imports all components
    init_path = components_dir / "__init__.py"
    with open(init_path, "w") as f:
        f.write('"""FIX component models."""\n\n')
        
        # Import all components
        for component_name in components:
            f.write(f"from .{component_name.lower()} import {component_name}Component\n")
        
        # Export all components
        f.write('\n__all__ = [\n')
        for component_name in components:
            f.write(f"    '{component_name}Component',\n")
        f.write(']\n')

    logger.info(f"Generated {len(components)} component models")

def fix_model_rebuild_calls(file_path: Path, component_name: str):
    """Fix model_rebuild() calls and __str__ method formatting in component files."""
    if not file_path.exists():
        return
    
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Fix truncated __str__ method if found
    """"
    str_method_pattern = r'def __str__\(self\) -> str:\n\s+fields = \[\]\n(.*?)return f"{self\.__class__\.__name__}'
    if '__str__' in content and 'return f"{self.__class__.__name__}' in content:
        if not re.search(r'return f"{self\.__class__\.__name__}\(\{.*?\}\)"', content):
            # Fix the truncated __str__ method
            content = re.sub(
                str_method_pattern,
                lambda m: m.group(0) + "({', '.join(fields)})",
                content
            )
    """
    # Ensure only one model_rebuild call at the end
    rebuild_pattern = r'# Rebuild model to resolve forward references\n.*?Component\.model_rebuild\(\)'
    
    # Remove any existing model_rebuild calls
    content = re.sub(rebuild_pattern, '', content)
    
    # Add proper model_rebuild call at the end
    if not content.endswith('\n\n'):
        content += '\n'
    content += f"\n# Rebuild model to resolve forward references\n{component_name}Component.model_rebuild()"
    
    with open(file_path, 'w') as f:
        f.write(content)

def generate_message_model(message_name: str, message: Dict, fields: Dict, components: Dict, output_dir: Path) -> None:
    """Generate a Pydantic model for a FIX message.
    
    Args:
        message_name: Name of the message
        message: Message definition dictionary
        fields: Dictionary of all fields
        components: Dictionary of all components
        output_dir: Output directory for generated files
    """
    # Convert message name to snake case for file name
    file_name = message_name.lower()
    file_path = output_dir / "messages" / f"{file_name}.py"
    
    # Collect imports
    imports = {
        'typing': {'Optional', 'List'},
        'datetime': {'date', 'datetime', 'time'},
        'pydantic': {'Field'},
        'base': {'FIXMessageBase'},
        'components': set()
    }
    
    # Add components from message definition
    for component in message.get('components', []):
        component_name = component['name']
        imports['components'].add(component_name)
    
    # Add components and groups from fields
    for field in message.get('fields', []):
        if 'component' in field:
            component_name = field['component']
            imports['components'].add(component_name)
        elif 'group' in field:
            group_name = field['group']
            imports['components'].add(group_name)
    
    with open(file_path, "w") as f:
        # Write docstring
        f.write('"""FIX message model for {name} ({msgtype}).\n\nCategory: {category}\n"""\n'.format(
            name=message_name,
            msgtype=message['msgtype'],
            category=message.get('category', '')
        ))
        
        # Write imports in a structured way
        if imports['typing']:
            f.write(f"from typing import {', '.join(sorted(imports['typing']))}\n")
        if imports['datetime']:
            f.write(f"from datetime import {', '.join(sorted(imports['datetime']))}\n")
        if imports['pydantic']:
            f.write(f"from pydantic import {', '.join(sorted(imports['pydantic']))}\n")
        if imports['base']:
            f.write(f"from ..base import {', '.join(sorted(imports['base']))}\n")
        
        # Write component imports
        for component_name in sorted(imports['components']):
            comp_class = f"{component_name}Component"
            f.write(f"from ..components.{component_name.lower()} import {comp_class}\n")
        
        f.write("\n")
        
        # Write class definition
        f.write(f"class {message_name}Message(FIXMessageBase):\n")
        f.write(f'    """FIX message model for {message_name}."""\n\n')
        
        # Override MsgType field with correct default value
        f.write(f'    MsgType: str = Field("{message["msgtype"]}", alias="35")\n\n')
        
        # Write components from message definition
        for component in message.get('components', []):
            component_name = component['name']
            required = component.get('required', False)
            f.write(f"    {component_name}: {'Optional[' if not required else ''}{component_name}Component{']' if not required else ''} = Field({'None' if not required else '...'}, description='')\n")
        
        # Write fields
        for field in message.get('fields', []):
            if 'component' in field:
                component_name = field['component']
                required = field.get('required', False)
                f.write(f"    {component_name}: {'Optional[' if not required else ''}{component_name}Component{']' if not required else ''} = Field({'None' if not required else '...'}, description='')\n")
            elif 'group' in field:
                group_name = field['group']
                required = field.get('required', False)
                f.write(f"    {group_name}: {'Optional[' if not required else ''}List[{group_name}Group]{']' if not required else ''} = Field({'None' if not required else '...'}, description='')\n")
            else:
                field_name = field['name']
                field_type = FIX_TYPE_MAP.get(field['type'], 'str')
                required = field.get('required', False)
                tag = field['number']
                description = field.get('description', '')
                f.write(f"    {field_name}: {'Optional[' if not required else ''}{field_type}{'] = Field(None' if not required else ' = Field(...'}, alias='{tag}', description='{description}')\n")
        
        f.write("\n")

def generate_message_models(
    messages: Dict[str, Dict[str, Any]], 
    output_dir: Path,
    fields: Dict[str, Dict[str, Any]],
    components: Dict[str, Dict[str, Any]]
) -> None:
    """Generate Pydantic models for all FIX messages.
    
    Args:
        messages: Dictionary of message definitions
        output_dir: Directory to write the model files
        fields: Dictionary of field definitions
        components: Dictionary of component definitions
    """
    # Create messages directory
    messages_dir = output_dir / 'messages'
    messages_dir.mkdir(exist_ok=True)
    
    # Clean up old message files
    logger.info("Cleaning up old message files...")
    for file in messages_dir.glob('*.py'):
        if file.name != '__init__.py':
            file.unlink()
    
    # Generate base classes
    generate_message_base(output_dir)
    
    # Generate message models
    for msg_name, message in messages.items():
        generate_message_model(msg_name, message, fields, components, output_dir)
    
    # Create __init__.py
    with open(messages_dir / '__init__.py', 'w') as f:
        f.write('"""\n')
        f.write('FIX message models.\n')
        f.write('"""\n\n')
        
        # Import all messages
        for msg_name in messages:
            f.write(f'from .{msg_name.lower()} import {msg_name}Message\n')
        
        # Export all messages
        f.write('\n__all__ = [\n')
        for msg_name in messages:
            f.write(f"    '{msg_name}Message',\n")
        f.write(']\n')

def generate_init_file(output_dir: Path, messages: Dict[str, FixMessage], components: Dict[str, FixComponent]):
    """Generate the main __init__.py file for the generated package."""
    logger.info("Generating main __init__.py file")
    
    init_path = output_dir / "__init__.py"
    with open(init_path, "w") as f:
        f.write('''"""
Generated FIX models from FIX 4.4 specification.

This package contains Pydantic models for FIX 4.4 messages, components, and fields.
"""

# Import message models
from .messages import FIXMessageBase
''')
        
        # Add imports for message classes
        for msg_name in sorted(messages.keys()):
            # Convert message name to lowercase for import
            file_name = msg_name.lower()
            f.write(f"from .messages.{file_name} import {msg_name}Message\n")
        
        f.write("\n# Import component models\n")
        f.write("from .components import FIXComponentBase\n")
        
        # Add imports for component classes
        for comp_name in sorted(components.keys()):
            f.write(f"from .components.{comp_name.lower()} import {comp_name}Component\n")
        
        f.write("\n# Import field base\n")
        f.write("from .fields import FIXFieldBase\n")
        
        # Add message types mapping
        f.write("\n# Message types mapping\n")
        f.write("MESSAGE_TYPES = {\n")
        for msg_name, msg in sorted(messages.items(), key=lambda x: x[0]):
            f.write(f"    '{msg.msgtype}': {msg_name}Message,\n")
        f.write("}\n")

def generate_models(spec_path: Path, output_dir: Path) -> None:
    """Generate FIX models from specification.
    
    Args:
        spec_path: Path to FIX specification XML file
        output_dir: Directory to write generated models
    """
    # Parse FIX specification
    fields, components, messages = parse_fix_spec(spec_path)
    
    # Create output directory
    output_dir.mkdir(exist_ok=True)
    
    # Generate field models
    generate_field_models(fields, output_dir)
    
    # Generate component models
    generate_component_models(components, output_dir, fields)
    
    # Generate message models
    generate_message_models(messages, output_dir, fields, components)
    
    # Create __init__.py
    with open(output_dir / '__init__.py', 'w') as f:
        f.write('"""\n')
        f.write('FIX models.\n')
        f.write('"""\n\n')
        
        # Import all models
        f.write('from .fields import *\n')
        f.write('from .components import *\n')
        f.write('from .messages import *\n')
        
        # Export all models
        f.write('\n__all__ = [\n')
        f.write("    'FIXFieldBase',\n")
        f.write("    'FIXComponentBase',\n")
        f.write("    'FIXMessageBase',\n")
        f.write(']\n')

def generate_message_base(output_dir: Path) -> None:
    """Generate the base message class.
    
    Args:
        output_dir: Directory to write the base class
    """
    # Create base directory
    base_dir = output_dir / 'base'
    base_dir.mkdir(exist_ok=True)
    
    # Generate base.py
    with open(base_dir / 'base.py', 'w') as f:
        f.write('"""\n')
        f.write('FIX message base class.\n')
        f.write('"""\n\n')
        f.write('from typing import Dict, Any\n')
        f.write('from pydantic import BaseModel, Field, ConfigDict\n\n')
        
        # Write FIXMessageBase class
        f.write('class FIXMessageBase(BaseModel):\n')
        f.write('    """\n')
        f.write('    Base class for FIX messages.\n')
        f.write('    """\n\n')
        
        f.write('    model_config = ConfigDict(\n')
        f.write('        populate_by_name=True,\n')
        f.write('        validate_assignment=True,\n')
        f.write('    )\n\n')
        
        # Standard FIX header fields
        f.write('    # Standard FIX header fields\n')
        f.write('    BeginString: str = Field(..., alias="8")\n')
        f.write('    BodyLength: int = Field(..., alias="9")\n')
        f.write('    MsgType: str = Field(..., alias="35")\n')
        f.write('    SenderCompID: str = Field(..., alias="49")\n')
        f.write('    TargetCompID: str = Field(..., alias="56")\n')
        f.write('    MsgSeqNum: int = Field(..., alias="34")\n')
        f.write('    SendingTime: str = Field(..., alias="52")\n')
        f.write('    CheckSum: str = Field(..., alias="10")\n\n')
        
        f.write('    def to_dict(self) -> Dict[str, Any]:\n')
        f.write('        """Convert message to dictionary."""\n')
        f.write('        return self.model_dump(by_alias=True)\n\n')
        
        f.write('    def __str__(self) -> str:\n')
        f.write('        """String representation of message."""\n')
        f.write('        fields = []\n')
        f.write('        for name, value in self.model_dump(by_alias=True).items():\n')
        f.write('            if value is not None:\n')
        f.write('                fields.append(f"{name}={value}")\n')
        f.write('        return f"{self.__class__.__name__}({", ".join(fields)})"\n\n')

        # Write FIXComponentBase class
        f.write('class FIXComponentBase(BaseModel):\n')
        f.write('    """\n')
        f.write('    Base class for FIX components.\n')
        f.write('    """\n\n')
        
        f.write('    model_config = ConfigDict(\n')
        f.write('        populate_by_name=True,\n')
        f.write('        validate_assignment=True,\n')
        f.write('    )\n\n')
        
        f.write('    def to_dict(self) -> Dict[str, Any]:\n')
        f.write('        """Convert component to dictionary."""\n')
        f.write('        return self.model_dump(by_alias=True)\n\n')
        
        f.write('    def __str__(self) -> str:\n')
        f.write('        """String representation of component."""\n')
        f.write('        fields = []\n')
        f.write('        for name, value in self.model_dump(by_alias=True).items():\n')
        f.write('            if value is not None:\n')
        f.write('                fields.append(f"{name}={value}")\n')
        f.write('        return f"{self.__class__.__name__}({", ".join(fields)})"\n')
        
    # Create __init__.py
    with open(base_dir / '__init__.py', 'w') as f:
        f.write('"""\n')
        f.write('FIX base classes.\n')
        f.write('"""\n\n')
        f.write('from .base import FIXMessageBase, FIXComponentBase\n\n')
        f.write('__all__ = [\n')
        f.write("    'FIXMessageBase',\n")
        f.write("    'FIXComponentBase',\n")
        f.write(']\n')

def main():
    """Main function to generate FIX models."""
    parser = argparse.ArgumentParser(description="Generate Pydantic models from FIX spec")
    parser.add_argument("--spec-file", type=str, required=True, help="Path to FIX spec XML file")
    parser.add_argument("--output-dir", type=str, required=True, help="Directory to output generated models")
    parser.add_argument("--log-level", type=str, default="INFO", help="Logging level")
    args = parser.parse_args()
    
    # Set up logging
    numeric_level = getattr(logging, args.log_level.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError(f"Invalid log level: {args.log_level}")
    logging.basicConfig(level=numeric_level, format="%(asctime)s [%(levelname)s] %(message)s")
    
    # Create output directories
    output_dir = Path(args.output_dir)
    components_dir = output_dir / "components"
    messages_dir = output_dir / "messages"
    fields_dir = output_dir / "fields"
    
    components_dir.mkdir(parents=True, exist_ok=True)
    messages_dir.mkdir(parents=True, exist_ok=True)
    fields_dir.mkdir(parents=True, exist_ok=True)
    
    logger.info(f"Loading FIX spec from {args.spec_file}")
    
    # Parse the FIX specification directly using the XML parser
    spec_path = Path(args.spec_file)
    generate_models(spec_path, output_dir)
    
    logger.info("FIX model generation complete")

if __name__ == "__main__":
    main() 