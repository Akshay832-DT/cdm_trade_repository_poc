#!/usr/bin/env python3
"""
FpML Pydantic Model Generator

This script generates Pydantic models from FpML schema files (XSD).
It creates a hierarchy of Python classes representing the FpML data model.
"""
import os
import sys
import logging
import xml.etree.ElementTree as ET
from pathlib import Path
import argparse
import re
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
DEFAULT_VERSION = "5-10"
SCHEMA_DIR = Path("specifications/fpml/xsd")
OUTPUT_DIR = Path("src/models/fpml/generated")
XS_NAMESPACE = "{http://www.w3.org/2001/XMLSchema}"
FPML_NAMESPACE = "http://www.fpml.org/FpML-5/confirmation"

# XML Schema type mapping to Python types
XS_TYPE_MAP = {
    "xs:string": "str",
    "xs:integer": "int",
    "xs:int": "int",
    "xs:positiveInteger": "int",
    "xs:nonNegativeInteger": "int",
    "xs:decimal": "float",
    "xs:double": "float",
    "xs:boolean": "bool",
    "xs:date": "date",
    "xs:time": "time",
    "xs:dateTime": "datetime",
    "xs:anyURI": "str",
    "xs:ID": "str",
    "xs:IDREF": "str",
    "xs:token": "str",
    "xs:normalizedString": "str",
    "xs:NMTOKEN": "str",
    "xs:NMTOKENS": "str",
    "xs:anyType": "Any",
}

@dataclass
class XsdElement:
    """Class for storing XSD element information."""
    name: str
    type_name: str = None
    min_occurs: int = 1
    max_occurs: int = 1
    documentation: str = ""
    is_complex: bool = False
    is_simple: bool = False
    is_enum: bool = False
    enum_values: List[str] = field(default_factory=list)
    sub_elements: List[Any] = field(default_factory=list)
    attributes: List[Any] = field(default_factory=list)
    
@dataclass
class XsdComplexType:
    """Class for storing XSD complex type information."""
    name: str
    documentation: str = ""
    elements: List[XsdElement] = field(default_factory=list)
    attributes: List[Any] = field(default_factory=list)
    base_type: str = None
    
@dataclass
class XsdSimpleType:
    """Class for storing XSD simple type information."""
    name: str
    documentation: str = ""
    base_type: str = None
    is_enum: bool = False
    enum_values: List[str] = field(default_factory=list)

def create_output_directories():
    """Create the necessary output directories."""
    OUTPUT_DIR.mkdir(exist_ok=True)
    (OUTPUT_DIR / "base").mkdir(exist_ok=True)
    (OUTPUT_DIR / "common").mkdir(exist_ok=True)
    (OUTPUT_DIR / "components").mkdir(exist_ok=True)
    (OUTPUT_DIR / "messages").mkdir(exist_ok=True)
    (OUTPUT_DIR / "trade").mkdir(exist_ok=True)
    (OUTPUT_DIR / "enums").mkdir(exist_ok=True)

def camel_to_snake(name):
    """Convert CamelCase to snake_case."""
    name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', name).lower()

def extract_local_name(qualified_name):
    """Extract local name from qualified name."""
    if ":" in qualified_name:
        return qualified_name.split(":")[-1]
    return qualified_name

def get_python_type(xsd_type: str) -> str:
    """Convert XSD type to Python type."""
    if not xsd_type:
        return "Any"
    
    # Check if type is already a Python type
    if xsd_type in ["str", "int", "float", "bool", "date", "datetime", "time", "Any"]:
        return xsd_type
    
    # Check if type is a mapped XSD type
    if xsd_type in XS_TYPE_MAP:
        return XS_TYPE_MAP[xsd_type]
    
    # If type has a namespace prefix, extract the local name
    local_type = extract_local_name(xsd_type)
    
    # Custom FpML type - will be a generated class
    return local_type

def topological_sort(types_dict: Dict[str, Any]) -> List[str]:
    """
    Sort types in topological order based on their dependencies.
    This ensures types are defined before they are referenced.
    
    Args:
        types_dict: Dictionary of types (name -> type object)
        
    Returns:
        List of type names in topological order
    """
    # Build dependency graph
    dependencies = {}
    for name, type_obj in types_dict.items():
        deps = set()
        
        # For complex types, track field dependencies
        if hasattr(type_obj, 'elements'):
            for element in type_obj.elements:
                if element.type_name and element.type_name in types_dict:
                    deps.add(element.type_name)
        
        # For simple types, track base type dependencies
        if hasattr(type_obj, 'base_type') and type_obj.base_type in types_dict:
            deps.add(type_obj.base_type)
            
        dependencies[name] = deps
    
    # Topological sort
    sorted_types = []
    visited = set()
    temp_visited = set()
    
    def visit(node):
        if node in temp_visited:
            # We've hit a cycle, skip this to avoid infinite recursion
            # This will be handled by forward references in the generated code
            return
        if node in visited:
            return
            
        temp_visited.add(node)
        for dep in dependencies.get(node, set()):
            visit(dep)
        temp_visited.remove(node)
        visited.add(node)
        sorted_types.append(node)
    
    # Visit all nodes
    for name in types_dict:
        if name not in visited:
            visit(name)
    
    return sorted_types

def parse_xsd_schemas(version: str) -> Tuple[Dict[str, XsdComplexType], Dict[str, XsdSimpleType], Dict[str, XsdElement]]:
    """Parse XSD schemas and extract type definitions.
    
    Args:
        version: FpML version (e.g., "5-10")
        
    Returns:
        Tuple of (complex_types, simple_types, elements)
    """
    schema_dir = SCHEMA_DIR / version
    schema_files = list(schema_dir.glob("*.xsd"))
    
    if not schema_files:
        logger.error(f"No schema files found for FpML {version}. Run fpml_schema_downloader.py first.")
        sys.exit(1)
    
    # Dictionaries to store parsed types and elements
    complex_types = {}
    simple_types = {}
    elements = {}
    
    # First pass - collect all type and element definitions
    for schema_file in schema_files:
        try:
            logger.info(f"Parsing schema file: {schema_file.name}")
            tree = ET.parse(schema_file)
            root = tree.getroot()
            
            # Parse complex types
            for complex_type in root.findall(f".//{XS_NAMESPACE}complexType"):
                name = complex_type.get("name")
                if not name:
                    continue
                
                documentation = ""
                doc_elem = complex_type.find(f".//{XS_NAMESPACE}documentation")
                if doc_elem is not None and doc_elem.text:
                    documentation = doc_elem.text.strip()
                
                # Find base type if this is an extension
                base_type = None
                extension = complex_type.find(f".//{XS_NAMESPACE}extension")
                if extension is not None:
                    base_type = extension.get("base")
                
                complex_types[name] = XsdComplexType(
                    name=name, 
                    documentation=documentation,
                    base_type=base_type
                )
            
            # Parse simple types
            for simple_type in root.findall(f".//{XS_NAMESPACE}simpleType"):
                name = simple_type.get("name")
                if not name:
                    continue
                
                documentation = ""
                doc_elem = simple_type.find(f".//{XS_NAMESPACE}documentation")
                if doc_elem is not None and doc_elem.text:
                    documentation = doc_elem.text.strip()
                
                # Find base type
                base_type = None
                restriction = simple_type.find(f".//{XS_NAMESPACE}restriction")
                if restriction is not None:
                    base_type = restriction.get("base")
                
                # Check if this is an enumeration
                is_enum = False
                enum_values = []
                if restriction is not None:
                    enums = restriction.findall(f".//{XS_NAMESPACE}enumeration")
                    if enums:
                        is_enum = True
                        enum_values = [e.get("value") for e in enums]
                
                simple_types[name] = XsdSimpleType(
                    name=name,
                    documentation=documentation,
                    base_type=base_type,
                    is_enum=is_enum,
                    enum_values=enum_values
                )
            
            # Parse elements
            for element in root.findall(f".//{XS_NAMESPACE}element"):
                name = element.get("name")
                if not name or name in elements:
                    continue
                
                type_name = element.get("type")
                
                documentation = ""
                doc_elem = element.find(f".//{XS_NAMESPACE}documentation")
                if doc_elem is not None and doc_elem.text:
                    documentation = doc_elem.text.strip()
                
                min_occurs = int(element.get("minOccurs", "1"))
                max_occurs_str = element.get("maxOccurs", "1")
                max_occurs = 999999 if max_occurs_str == "unbounded" else int(max_occurs_str)
                
                elements[name] = XsdElement(
                    name=name,
                    type_name=type_name,
                    min_occurs=min_occurs,
                    max_occurs=max_occurs,
                    documentation=documentation
                )
        
        except ET.ParseError as e:
            logger.error(f"Error parsing {schema_file}: {str(e)}")
            continue
    
    # Second pass - resolve element references and complex type contents
    for schema_file in schema_files:
        try:
            tree = ET.parse(schema_file)
            root = tree.getroot()
            
            # Process complex type elements
            for complex_type_elem in root.findall(f".//{XS_NAMESPACE}complexType"):
                name = complex_type_elem.get("name")
                if not name or name not in complex_types:
                    continue
                
                complex_type = complex_types[name]
                
                # Process direct child elements
                for element in complex_type_elem.findall(f".//{XS_NAMESPACE}element"):
                    elem_name = element.get("name")
                    if not elem_name:
                        ref = element.get("ref")
                        if ref:
                            elem_name = extract_local_name(ref)
                    
                    elem_type = element.get("type")
                    min_occurs = int(element.get("minOccurs", "1"))
                    max_occurs_str = element.get("maxOccurs", "1")
                    max_occurs = 999999 if max_occurs_str == "unbounded" else int(max_occurs_str)
                    
                    documentation = ""
                    doc_elem = element.find(f".//{XS_NAMESPACE}documentation")
                    if doc_elem is not None and doc_elem.text:
                        documentation = doc_elem.text.strip()
                    
                    complex_type.elements.append(XsdElement(
                        name=elem_name,
                        type_name=elem_type,
                        min_occurs=min_occurs,
                        max_occurs=max_occurs,
                        documentation=documentation
                    ))
                
                # Process attributes
                for attribute in complex_type_elem.findall(f".//{XS_NAMESPACE}attribute"):
                    attr_name = attribute.get("name")
                    attr_type = attribute.get("type")
                    attr_use = attribute.get("use", "optional")
                    
                    if attr_name and attr_type:
                        complex_type.attributes.append({
                            "name": attr_name,
                            "type": attr_type,
                            "required": attr_use == "required"
                        })
        
        except ET.ParseError:
            continue
    
    logger.info(f"Parsed {len(complex_types)} complex types, {len(simple_types)} simple types, and {len(elements)} elements")
    return complex_types, simple_types, elements

def generate_base_classes():
    """Generate base classes for FpML models."""
    base_dir = OUTPUT_DIR / "base"
    base_dir.mkdir(exist_ok=True)
    
    # Generate base.py
    with open(base_dir / "base.py", "w") as f:
        f.write('''"""
Base classes for FpML models.
"""
from pydantic import BaseModel, Field
from typing import Dict, Any, Optional, List, ForwardRef, TYPE_CHECKING
from datetime import date, datetime, time

class FpMLModelBase(BaseModel):
    """Base class for all FpML models."""
    class Config:
        populate_by_field_name = True
        validate_assignment = True
        extra = 'forbid'
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert the model to a dictionary."""
        return self.dict()
    
    def __str__(self) -> str:
        """Convert the model to a string."""
        fields = []
        for field_name, field_value in self.dict().items():
            if field_value is not None:
                fields.append(f"{field_name}={field_value}")
        return f"{self.__class__.__name__}({', '.join(fields)})"

class FpMLTradeBase(FpMLModelBase):
    """Base class for FpML trades."""
    pass

class FpMLComponentBase(FpMLModelBase):
    """Base class for FpML components."""
    pass

class FpMLMessageBase(FpMLModelBase):
    """Base class for FpML messages."""
    pass
''')
    
    # Generate __init__.py
    with open(base_dir / "__init__.py", "w") as f:
        f.write('''"""
Base classes for FpML models.
"""
from .base import FpMLModelBase, FpMLTradeBase, FpMLComponentBase, FpMLMessageBase

__all__ = [
    "FpMLModelBase",
    "FpMLTradeBase",
    "FpMLComponentBase",
    "FpMLMessageBase"
]
''')
    
    # Generate root __init__.py
    with open(OUTPUT_DIR / "__init__.py", "w") as f:
        f.write('''"""
Generated FpML model classes.
"""
# Import base classes first to avoid circular imports
from .base.base import FpMLModelBase, FpMLTradeBase, FpMLComponentBase, FpMLMessageBase

# Import enums (these have no dependencies)
from .enums.payment_frequency_enum import PaymentFrequencyEnum
from .enums.currency_enum import CurrencyEnum
from .enums.credit_event_enum import CreditEventEnum
from .enums.settlement_type_enum import SettlementTypeEnum

# Import common types in dependency order
from .common.party_reference_type import PartyReferenceType
from .common.party_trade_identifier_type import PartyTradeIdentifierType
from .common.trade_header_type import TradeHeaderType
from .common.payer_receiver_type import PayerReceiverType
from .common.notional_amount_type import NotionalAmountType
from .common.swap_stream_type import SwapStreamType
from .common.interest_rate_product_type import InterestRateProductType
from .common.protection_terms_type import ProtectionTermsType
from .common.reference_information_type import ReferenceInformationType
from .common.credit_product_type import CreditProductType
from .common.product_type import ProductType
from .common.trade_type import TradeType
from .common.fp_ml_type import FpMLType

# Import trade models 
from .trade.trade import (
    PartyReference, PartyTradeIdentifier, TradeHeader, 
    PayerReceiver, NotionalAmount, SwapStream, 
    InterestRateProduct, ProtectionTerms, ReferenceInformation,
    CreditProduct, Product, FpMLTrade
)

__all__ = [
    "FpMLModelBase",
    "FpMLTradeBase", 
    "FpMLComponentBase",
    "FpMLMessageBase",
    "FpMLTrade",
    
    # Enums
    "PaymentFrequencyEnum",
    "CurrencyEnum",
    "CreditEventEnum",
    "SettlementTypeEnum",
    
    # Common types
    "PartyReferenceType",
    "PartyTradeIdentifierType",
    "TradeHeaderType",
    "PayerReceiverType",
    "NotionalAmountType",
    "SwapStreamType",
    "InterestRateProductType",
    "ProtectionTermsType",
    "ReferenceInformationType",
    "CreditProductType",
    "ProductType",
    "TradeType",
    "FpMLType",
    
    # Trade components
    "PartyReference",
    "PartyTradeIdentifier",
    "TradeHeader",
    "PayerReceiver",
    "NotionalAmount", 
    "SwapStream",
    "InterestRateProduct",
    "ProtectionTerms",
    "ReferenceInformation",
    "CreditProduct",
    "Product"
]
''')

def generate_enum_models(simple_types: Dict[str, XsdSimpleType]):
    """Generate Pydantic models for enumerations."""
    enums_dir = OUTPUT_DIR / "enums"
    enums_dir.mkdir(exist_ok=True)
    
    # Get all enum types
    enum_types = {name: stype for name, stype in simple_types.items() 
                 if stype.is_enum and stype.enum_values}
    
    # Sort enum types in topological order
    sorted_enum_names = topological_sort(enum_types)
    
    # Create __init__.py with properly ordered imports
    with open(enums_dir / "__init__.py", "w") as f:
        f.write('"""FpML enumeration types."""\n\n')
        
        # Import all enums in topological order
        if sorted_enum_names:
            for enum_name in sorted_enum_names:
                snake_name = camel_to_snake(enum_name)
                f.write(f"from .{snake_name} import {enum_name}\n")
            
            f.write("\n__all__ = [\n")
            for enum_name in sorted_enum_names:
                f.write(f'    "{enum_name}",\n')
            f.write("]\n")
    
    # Generate enum classes
    enum_count = 0
    for name, stype in enum_types.items():
        snake_name = camel_to_snake(name)
        file_path = enums_dir / f"{snake_name}.py"
        
        with open(file_path, "w") as f:
            f.write(f'"""\nFpML Enumeration Type - {name}\n"""\n\n')
            f.write("from enum import Enum\n\n")
            
            f.write(f"class {name}(str, Enum):\n")
            if stype.documentation:
                f.write(f'    """{stype.documentation}"""\n\n')
            
            # Write enum values
            for value in stype.enum_values:
                # Clean value to make it a valid Python identifier
                clean_value = re.sub(r'\W|^(?=\d)', '_', value)
                if not clean_value:
                    clean_value = f"VALUE_{value}"
                
                f.write(f'    {clean_value} = "{value}"\n')
        
        enum_count += 1
    
    logger.info(f"Generated {enum_count} enumeration models")

def generate_type_models(complex_types: Dict[str, XsdComplexType], simple_types: Dict[str, XsdSimpleType]):
    """Generate Pydantic models for complex types."""
    common_dir = OUTPUT_DIR / "common"
    common_dir.mkdir(exist_ok=True)
    
    # Filter complex types - skip very large ones
    filtered_types = {name: ctype for name, ctype in complex_types.items() 
                     if len(ctype.elements) <= 30}
    
    # Sort complex types in topological order
    sorted_type_names = topological_sort(filtered_types)
    
    # Create __init__.py with properly ordered imports
    with open(common_dir / "__init__.py", "w") as f:
        f.write('"""FpML common types."""\n\n')
        
        # Import all types in topological order
        if sorted_type_names:
            for type_name in sorted_type_names:
                snake_name = camel_to_snake(type_name)
                f.write(f"from .{snake_name} import {type_name}\n")
            
            f.write("\n__all__ = [\n")
            for type_name in sorted_type_names:
                f.write(f'    "{type_name}",\n')
            f.write("]\n")
    
    # Process complex types
    for name in sorted_type_names:
        ctype = filtered_types[name]
        
        # Create model file
        snake_name = camel_to_snake(name)
        file_path = common_dir / f"{snake_name}.py"
        
        with open(file_path, "w") as f:
            f.write(f'"""\nFpML Complex Type - {name}\n"""\n\n')
            
            # Imports
            f.write("from typing import List, Optional, Any, Dict, ForwardRef, TYPE_CHECKING\n")
            f.write("from pydantic import Field\n")
            f.write("from datetime import date, datetime, time\n")
            f.write("from ..base import FpMLModelBase\n\n")
            
            # Import enums if needed
            enum_imports = set()
            for element in ctype.elements:
                if element.type_name in simple_types and simple_types[element.type_name].is_enum:
                    enum_name = element.type_name
                    snake_enum = camel_to_snake(enum_name)
                    enum_imports.add(f"from ..enums.{snake_enum} import {enum_name}")
            
            # Import forward references for complex types
            forward_refs = set()
            for element in ctype.elements:
                if element.type_name in complex_types and element.type_name != name:
                    ref_name = element.type_name
                    forward_refs.add(ref_name)
            
            # Direct imports for other types (no conditional imports)
            if forward_refs:
                f.write("# Import directly for use at runtime\n")
                for ref_name in sorted(forward_refs):
                    snake_ref = camel_to_snake(ref_name)
                    f.write(f"from .{snake_ref} import {ref_name}\n")
                f.write("\n")
                
                # Define ForwardRef variables
                f.write("# Only use the forward references for type checking\n")
                for ref_name in sorted(forward_refs):
                    f.write(f"{ref_name}Ref = ForwardRef('{ref_name}')\n")
                f.write("\n")
            
            for enum_import in sorted(enum_imports):
                f.write(f"{enum_import}\n")
            
            if enum_imports:
                f.write("\n")
            
            # Class definition
            base_class = ctype.base_type if ctype.base_type else "FpMLModelBase"
            if base_class and not base_class.startswith("FpML"):
                base_class = "FpMLModelBase"
            
            f.write(f"class {name}({base_class}):\n")
            if ctype.documentation:
                f.write(f'    """{ctype.documentation}"""\n\n')
            
            # Model config
            f.write("    class Config:\n")
            f.write("        populate_by_field_name = True\n")
            f.write("        validate_assignment = True\n\n")
            
            # Fields
            if not ctype.elements and not ctype.attributes:
                f.write("    pass\n")
            else:
                for element in ctype.elements:
                    field_name = element.name
                    field_type = get_python_type(element.type_name)
                    
                    # Use actual class names, not forward refs
                    # This is the key change to avoid circular dependency issues
                    # Use the actual type instead of ForwardRef
                    
                    # Check if this should be a List
                    if element.max_occurs > 1:
                        field_type = f"List[{field_type}]"
                    
                    # Check if this is optional
                    if element.min_occurs == 0:
                        field_type = f"Optional[{field_type}]"
                        f.write(f"    {field_name}: {field_type} = Field(None")
                    else:
                        f.write(f"    {field_name}: {field_type} = Field(")
                    
                    # Add description if available
                    if element.documentation:
                        doc = element.documentation.replace("'", "\\'").replace('"', '\\"')
                        f.write(f', description="{doc}"')
                    
                    f.write(")\n")
                
                # Add attributes
                for attr in ctype.attributes:
                    attr_name = attr["name"]
                    attr_type = get_python_type(attr["type"])
                    
                    # Check if this is optional
                    if not attr["required"]:
                        attr_type = f"Optional[{attr_type}]"
                        f.write(f"    {attr_name}: {attr_type} = Field(None, alias='@{attr_name}')\n")
                    else:
                        f.write(f"    {attr_name}: {attr_type} = Field(alias='@{attr_name}')\n")
            
            # Add update_forward_refs call
            f.write("\n# Update forward references\n")
            f.write(f"{name}.update_forward_refs()\n")

def generate_trade_models(elements: Dict[str, XsdElement], complex_types: Dict[str, XsdComplexType]):
    """Generate trade-specific models."""
    trade_dir = OUTPUT_DIR / "trade"
    trade_dir.mkdir(exist_ok=True)
    
    # Create __init__.py
    with open(trade_dir / "__init__.py", "w") as f:
        f.write('"""FpML trade models."""\n\n')
        f.write("from .trade import FpMLTrade\n\n")
        f.write("__all__ = [\n")
        f.write('    "FpMLTrade"\n')
        f.write("]\n")
    
    # Generate trade model
    # In a real implementation, this would be generated from the schema
    # but for this example we'll create a basic model by hand
    with open(trade_dir / "trade.py", "w") as f:
        f.write('''"""
FpML Trade Model
"""
from typing import List, Optional, Dict, Any, Union, ForwardRef, TYPE_CHECKING
from pydantic import Field
from datetime import date, datetime
from ..base import FpMLTradeBase

# Define forward references for type checking only
PartyReferenceRef = ForwardRef('PartyReference')
PartyTradeIdentifierRef = ForwardRef('PartyTradeIdentifier')
TradeHeaderRef = ForwardRef('TradeHeader')
PayerReceiverRef = ForwardRef('PayerReceiver')
NotionalAmountRef = ForwardRef('NotionalAmount')
SwapStreamRef = ForwardRef('SwapStream')
InterestRateProductRef = ForwardRef('InterestRateProduct')
ProtectionTermsRef = ForwardRef('ProtectionTerms')
ReferenceInformationRef = ForwardRef('ReferenceInformation')
CreditProductRef = ForwardRef('CreditProduct')
ProductRef = ForwardRef('Product')

class PartyReference(FpMLTradeBase):
    """Reference to a party."""
    href: str = Field(alias="@href")

class PartyTradeIdentifier(FpMLTradeBase):
    """Trade identifier for a party."""
    partyReference: PartyReference
    tradeId: str
    
class TradeHeader(FpMLTradeBase):
    """Trade header information."""
    partyTradeIdentifier: List[PartyTradeIdentifier]
    tradeDate: date
    clearedDate: Optional[date] = None

class PayerReceiver(FpMLTradeBase):
    """Payer and receiver information."""
    payerPartyReference: PartyReference
    receiverPartyReference: PartyReference

class NotionalAmount(FpMLTradeBase):
    """Notional amount."""
    amount: float
    currency: str

class SwapStream(FpMLTradeBase):
    """Swap stream."""
    payerReceiver: PayerReceiver
    paymentFrequency: str
    notionalAmount: NotionalAmount

class InterestRateProduct(FpMLTradeBase):
    """Interest rate product."""
    swapStream: List[SwapStream]

class ProtectionTerms(FpMLTradeBase):
    """Credit derivative protection terms."""
    referenceEntity: str
    creditEvent: str
    settlementType: str

class ReferenceInformation(FpMLTradeBase):
    """Credit derivative reference information."""
    referenceEntity: str
    referenceObligation: Optional[str] = None

class CreditProduct(FpMLTradeBase):
    """Credit derivative product."""
    protectionTerms: ProtectionTerms
    referenceInformation: ReferenceInformation

class Product(FpMLTradeBase):
    """Trade product."""
    interestRate: Optional[InterestRateProduct] = None
    credit: Optional[CreditProduct] = None

class FpMLTrade(FpMLTradeBase):
    """FpML trade model."""
    tradeHeader: TradeHeader
    product: Product
    
    class Config:
        populate_by_field_name = True

# Update forward references
PartyReference.update_forward_refs()
PartyTradeIdentifier.update_forward_refs()
TradeHeader.update_forward_refs()
PayerReceiver.update_forward_refs()
NotionalAmount.update_forward_refs()
SwapStream.update_forward_refs()
InterestRateProduct.update_forward_refs()
ProtectionTerms.update_forward_refs()
ReferenceInformation.update_forward_refs()
CreditProduct.update_forward_refs()
Product.update_forward_refs()
FpMLTrade.update_forward_refs()
''')

def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(description="Generate Pydantic models from FpML schemas")
    parser.add_argument(
        "--version", 
        default=DEFAULT_VERSION,
        help=f"FpML version (default: {DEFAULT_VERSION})"
    )
    parser.add_argument(
        "--force", 
        action="store_true", 
        help="Force regeneration of models"
    )
    args = parser.parse_args()
    
    # Create output directories
    if args.force and OUTPUT_DIR.exists():
        shutil.rmtree(OUTPUT_DIR)
    create_output_directories()
    
    # Parse XSD schemas
    complex_types, simple_types, elements = parse_xsd_schemas(args.version)
    
    # Generate models in the correct dependency order
    # 1. Base classes first (has no dependencies)
    logger.info("Generating base classes...")
    generate_base_classes()
    
    # 2. Enums second (may depend on base classes)
    logger.info("Generating enum models...")
    generate_enum_models(simple_types)
    
    # 3. Common types third (may depend on base classes and enums)
    logger.info("Generating common type models...")
    generate_type_models(complex_types, simple_types)
    
    # 4. Trade models last (depend on all other models)
    logger.info("Generating trade models...")
    generate_trade_models(elements, complex_types)
    
    logger.info(f"Successfully generated FpML models for version {args.version}")

if __name__ == "__main__":
    main()