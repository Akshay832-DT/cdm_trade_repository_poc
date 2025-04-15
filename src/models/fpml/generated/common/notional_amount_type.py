"""
FpML Complex Type - NotionalAmountType
"""

from typing import List, Optional, Any, Dict, ForwardRef, TYPE_CHECKING
from pydantic import Field
from datetime import date, datetime, time
from ..base import FpMLModelBase

from ..enums.currency_enum import CurrencyEnum

class NotionalAmountType(FpMLModelBase):
    class Config:
        populate_by_field_name = True
        validate_assignment = True

    amount: float = Field()
    currency: CurrencyEnum = Field()

# Update forward references
NotionalAmountType.update_forward_refs()
