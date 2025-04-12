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
    """Convert a PascalCase name to camelCase."""
    return name[0].lower() + name[1:] if name else name

def generate_component_models(components, fields):
    """
    Generate Pydantic models for FIX components.
    
    Args:
        components: Dictionary of component definitions from the specification
        fields: Dictionary of field definitions from the specification
    """
    logger.info("Generating component models...")
    
    # Create the components directory if it doesn't exist
    os.makedirs(OUTPUT_DIR / "components", exist_ok=True)
    
    # Create the __init__.py file for the components directory
    with open(OUTPUT_DIR / "components" / "__init__.py", 'w') as init_file:
        init_file.write('''"""
FIX 4.4 Component Models

This package contains Pydantic models for FIX 4.4 components.
"""
''')
        
        # Generate a model for each component
        for component_name, component_fields in components.items():
            file_name = f"{component_name.lower()}.py"
            component_file_path = OUTPUT_DIR / "components" / file_name
            
            with open(component_file_path, 'w') as f:
                f.write(f'''"""
FIX 4.4 {component_name} Component

This module contains the Pydantic model for the {component_name} component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXMessageBase
''')
                
                # Special case for BidCompRspGrp
                if component_name == "BidCompRspGrp":
                    # Add import for CommissionData
                    f.write("from src.models.fix.generated.components.commissiondata import CommissionData\n")
                    
                    f.write(f'''

class NoBidComponents(FIXMessageBase):
    """
    NoBidComponents group fields
    """
    model_config = ConfigDict(
        populate_by_name=True,
        validate_by_name=True,
        json_encoders={{
            datetime: lambda v: v.isoformat(),
            date: lambda v: v.isoformat(),
            time: lambda v: v.isoformat()
        }}
    )
''')
                    # Add fields to the NoBidComponents group
                    for field in component_fields:
                        field_name = field['name'].replace(" ", "")
                        field_name = to_camel_case(field_name)  # Convert to camelCase
                        required = field['required']
                        
                        # Skip the NoBidComponents field (it's a count field)
                        if field_name == "noBidComponents":
                            continue
                        
                        # Special handling for CommissionData
                        if field_name == "commissionData":
                            f.write("    commissionData: Optional[CommissionData] = None\n")
                            continue
                        
                        # Get field type information
                        field_info = fields.get(field['name'].replace(" ", ""), {})  # Use original name for lookup
                        fix_type = field_info.get('type', 'STRING')
                        python_type = FIX_TYPE_MAP.get(fix_type, 'str')
                        
                        # Make the field optional if not required
                        if not required:
                            python_type = f"Optional[{python_type}]"
                        
                        # Add field to the model with proper Field alias
                        if 'tag' in field_info:
                            f.write(f"    {field_name}: {python_type} = Field(None, description='{field_info.get('description', '')}', alias='{field_info['tag']}')\n")
                        else:
                            f.write(f"    {field_name}: {python_type} = Field(None)\n")
                    
                    # Add the NoBidComponents field to BidCompRspGrp
                    f.write(f'''

class {component_name}(FIXMessageBase):
    """
    FIX 4.4 {component_name} Component
    """
    model_config = ConfigDict(
        populate_by_name=True,
        validate_by_name=True,
        json_encoders={{
            datetime: lambda v: v.isoformat(),
            date: lambda v: v.isoformat(),
            time: lambda v: v.isoformat()
        }}
    )
    
    # Count field for the number of bid components
    noBidComponents: Optional[int] = Field(None, description='Number of bid components', alias='420')
    
    # List of bid components
    noBidComponents_Items: List[NoBidComponents] = Field(default_factory=list)
''')
                else:
                    # Handle regular components
                    f.write(f'''

class {component_name}(FIXMessageBase):
    """
    FIX 4.4 {component_name} Component
    """
    model_config = ConfigDict(
        populate_by_name=True,
        validate_by_name=True,
        json_encoders={{
            datetime: lambda v: v.isoformat(),
            date: lambda v: v.isoformat(),
            time: lambda v: v.isoformat()
        }}
    )
''')
                    # Add fields to the component model
                    for field in component_fields:
                        if field.get('is_group'):
                            # Handle group fields
                            group_name = field['name'].replace(" ", "")
                            f.write(f'''

class {group_name}(FIXMessageBase):
    """
    {field['name']} group fields
    """
    model_config = ConfigDict(
        populate_by_name=True,
        validate_by_name=True,
        json_encoders={{
            datetime: lambda v: v.isoformat(),
            date: lambda v: v.isoformat(),
            time: lambda v: v.isoformat()
        }}
    )
''')
                            for group_field in field['fields']:
                                field_name = group_field['name'].replace(" ", "")
                                field_name = to_camel_case(field_name)  # Convert to camelCase
                                required = group_field['required']
                                
                                # Get field type information
                                field_info = fields.get(field['name'].replace(" ", ""), {})  # Use original name for lookup
                                fix_type = field_info.get('type', 'STRING')
                                python_type = FIX_TYPE_MAP.get(fix_type, 'str')
                                
                                # Make the field optional if not required
                                if not required:
                                    python_type = f"Optional[{python_type}]"
                                
                                # Add field to the model with proper Field alias
                                if 'tag' in field_info:
                                    f.write(f"    {field_name}: {python_type} = Field(None, description='{field_info.get('description', '')}', alias='{field_info['tag']}')\n")
                                else:
                                    f.write(f"    {field_name}: {python_type} = Field(None)\n")
                            
                            # Add the group to the component
                            group_name_camel = to_camel_case(group_name)  # Convert to camelCase
                            f.write(f"\n    {group_name_camel}s: List[{group_name}] = Field(default_factory=list)\n")
                        else:
                            # Handle regular fields
                            field_name = field['name'].replace(" ", "")
                            field_name = to_camel_case(field_name)  # Convert to camelCase
                            required = field['required']
                            
                            # Get field type information
                            field_info = fields.get(field['name'].replace(" ", ""), {})  # Use original name for lookup
                            fix_type = field_info.get('type', 'STRING')
                            python_type = FIX_TYPE_MAP.get(fix_type, 'str')
                            
                            # Make the field optional if not required
                            if not required:
                                python_type = f"Optional[{python_type}]"
                            
                            # Add field to the model with proper Field alias
                            if 'tag' in field_info:
                                f.write(f"    {field_name}: {python_type} = Field(None, description='{field_info.get('description', '')}', alias='{field_info['tag']}')\n")
                            else:
                                f.write(f"    {field_name}: {python_type} = Field(None)\n")
            
            # Add an import statement to the __init__.py file
            init_file.write(f"from .{component_name.lower()} import {component_name}\n")

def generate_message_models(messages, fields):
    """
    Generate Pydantic models for FIX messages.
    
    Args:
        messages: Dictionary of message type definitions from the specification
        fields: Dictionary of field definitions from the specification
    """
    logger.info("Generating message models...")
    
    # Define header/trailer fields that are already in FIXMessageBase
    base_fields = {
        'BeginString', 'BodyLength', 'MsgType', 'SenderCompID', 'TargetCompID',
        'MsgSeqNum', 'SendingTime', 'CheckSum'
    }
    
    # Create the messages directory if it doesn't exist
    os.makedirs(OUTPUT_DIR / "messages", exist_ok=True)
    
    # Create the __init__.py file for the messages directory
    with open(OUTPUT_DIR / "messages" / "__init__.py", 'w') as init_file:
        init_file.write('''"""
FIX 4.4 Message Models

This package contains Pydantic models for FIX 4.4 messages.
"""
''')
        
        # Generate a model for each message type
        for msg_name, msg_info in messages.items():
            file_name = f"{msg_name.lower()}.py"
            message_file_path = OUTPUT_DIR / "messages" / file_name
            
            with open(message_file_path, 'w') as f:
                f.write(f'''"""
FIX 4.4 {msg_name} Message

This module contains the Pydantic model for the {msg_name} message.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.fields.common import *
''')
                
                # Track components and groups we need to import
                components_to_import = set()
                groups_to_import = set()
                
                # First pass: collect all components and groups
                for field in msg_info['fields']:
                    if field.get('is_component'):
                        comp_name = field['name'].replace(" ", "")
                        components_to_import.add(comp_name)
                    elif field.get('is_group'):
                        group_name = field['name'].replace(" ", "")
                        groups_to_import.add(group_name)
                
                # Add imports for components and groups
                for comp_name in sorted(components_to_import):
                    f.write(f"from src.models.fix.generated.components.{comp_name.lower()} import {comp_name}\n")
                
                # Generate the message class
                f.write(f'''

class {msg_name}(FIXMessageBase):
    """
    FIX 4.4 {msg_name} Message
    """
    model_config = ConfigDict(
        populate_by_name=True,
        validate_by_name=True,
        json_encoders={{
            datetime: lambda v: v.isoformat(),
            date: lambda v: v.isoformat(),
            time: lambda v: v.isoformat()
        }}
    )
    
    # Set the message type for this message
    msgType: Literal["{msg_info.get('msgtype', '')}"] = Field("{msg_info.get('msgtype', '')}", alias='35')
    
    # Message-specific fields
''')
                
                # Generate fields
                for field in msg_info['fields']:
                    # Skip fields that are already in the base class
                    if field['name'].replace(" ", "") in base_fields:
                        continue
                        
                    if field.get('is_component'):
                        comp_name = field['name'].replace(" ", "")
                        field_name = to_camel_case(comp_name)  # Convert to camelCase
                        f.write(f"    {field_name}: Optional[{comp_name}] = Field(None, description='{comp_name} component')\n")
                    elif field.get('is_group'):
                        group_name = field['name'].replace(" ", "")
                        field_name = to_camel_case(group_name)  # Convert to camelCase
                        f.write(f"    {field_name}: Optional[List[{group_name}]] = Field(default_factory=list, description='{group_name} group')\n")
                    else:
                        field_name = field['name'].replace(" ", "")
                        field_name = to_camel_case(field_name)  # Convert to camelCase
                        field_type = FIX_TYPE_MAP.get(field['type'], 'str')
                        if field_type.startswith('List'):
                            f.write(f"    {field_name}: Optional[{field_type}] = Field(default_factory=list, description='', alias='{field['tag']}')\n")
                        else:
                            f.write(f"    {field_name}: Optional[{field_type}] = Field(None, description='', alias='{field['tag']}')\n")
                
                # Add model_dump method
                f.write('''
    def model_dump(self, **kwargs) -> Dict[str, Any]:
        """Override model_dump to handle nested components"""
        kwargs.setdefault('by_alias', True)
        data = super().model_dump(**kwargs)
        
        # Handle repeating components
        for field_name, value in data.items():
            if isinstance(value, list):
                # Set the No* field based on list length
                no_field = f"no{field_name}"  # Convert to camelCase
                if hasattr(self, no_field):
                    setattr(self, no_field, len(value))
        
        return data
''')
            
            # Add an import statement to the __init__.py file
            init_file.write(f"from .{msg_name.lower()} import {msg_name}\n")

def generate_base_models():
    """Generate base models for FIX messages."""
    logger.info("Generating base models...")
    
    with open(OUTPUT_DIR / "base.py", 'w') as f:
        f.write('''"""
FIX 4.4 Base Models

This module contains base models for FIX 4.4 messages.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from ...base import TradeModel

class FIXMessageBase(TradeModel):
    """
    Base class for all FIX messages.
    
    This includes common header and trailer fields.
    """
    model_config = ConfigDict(
        populate_by_name=True,
        validate_by_name=True,
        json_encoders={
            datetime: lambda v: v.isoformat(),
            date: lambda v: v.isoformat(),
            time: lambda v: v.isoformat()
        }
    )

    beginString: Literal["FIX.4.4"] = Field("FIX.4.4", alias='8')
    bodyLength: Optional[int] = Field(None, alias='9')
    msgType: str = Field(..., alias='35')
    senderCompID: str = Field(..., alias='49')
    targetCompID: str = Field(..., alias='56')
    msgSeqNum: int = Field(..., alias='34')
    sendingTime: datetime = Field(..., alias='52')
    checkSum: Optional[str] = Field(None, alias='10')
    
    # Additional fields will be stored in a dictionary
    additional_fields: Dict[str, Any] = Field(default_factory=dict)

    def model_dump(self, **kwargs) -> Dict[str, Any]:
        """
        Convert the message to a dictionary representation.
        
        Returns:
            Dict[str, Any]: Dictionary representation of the message
        """
        # Get base fields
        data = super().model_dump(**kwargs)
        # Add additional fields
        if self.additional_fields:
            data.update(self.additional_fields)
        return {k: v for k, v in data.items() if v is not None}
''')

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
    
    # Generate base models
    logger.info("Generating base models...")
    generate_base_models()
    
    # Parse FIX specification
    spec_data = parse_fix_spec(str(LOCAL_SPEC_PATH))
    if not spec_data:
        logger.error("Failed to parse FIX 4.4 specification")
        sys.exit(1)
    
    # Generate field models
    generate_field_models(spec_data['fields'])
    
    # Generate component models
    generate_component_models(spec_data['components'], spec_data['fields'])
    
    # Generate message models
    generate_message_models(spec_data['messages'], spec_data['fields'])
    
    # Generate __init__.py
    generate_init_file()
    
    logger.info(f"Successfully generated FIX 4.4 Pydantic models in {OUTPUT_DIR}")

if __name__ == "__main__":
    main() 