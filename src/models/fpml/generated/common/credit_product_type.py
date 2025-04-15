"""
FpML Complex Type - CreditProductType
"""

from typing import List, Optional, Any, Dict, ForwardRef, TYPE_CHECKING
from pydantic import Field
from datetime import date, datetime, time
from ..base import FpMLModelBase

# Import directly for use at runtime
from .protection_terms_type import ProtectionTermsType
from .reference_information_type import ReferenceInformationType

# Only use the forward references for type checking
ProtectionTermsTypeRef = ForwardRef('ProtectionTermsType')
ReferenceInformationTypeRef = ForwardRef('ReferenceInformationType')

class CreditProductType(FpMLModelBase):
    class Config:
        populate_by_field_name = True
        validate_assignment = True

    protectionTerms: ProtectionTermsType = Field()
    referenceInformation: ReferenceInformationType = Field()

# Update forward references
CreditProductType.update_forward_refs()
