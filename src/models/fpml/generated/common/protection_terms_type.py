"""
FpML Complex Type - ProtectionTermsType
"""

from typing import List, Optional, Any, Dict, ForwardRef, TYPE_CHECKING
from pydantic import Field
from datetime import date, datetime, time
from ..base import FpMLModelBase

from ..enums.credit_event_enum import CreditEventEnum
from ..enums.settlement_type_enum import SettlementTypeEnum

class ProtectionTermsType(FpMLModelBase):
    class Config:
        populate_by_field_name = True
        validate_assignment = True

    referenceEntity: str = Field()
    creditEvent: CreditEventEnum = Field()
    settlementType: SettlementTypeEnum = Field()

# Update forward references
ProtectionTermsType.update_forward_refs()
