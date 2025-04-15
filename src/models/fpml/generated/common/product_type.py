"""
FpML Complex Type - ProductType
"""

from typing import List, Optional, Any, Dict, ForwardRef, TYPE_CHECKING
from pydantic import Field
from datetime import date, datetime, time
from ..base import FpMLModelBase

# Import directly for use at runtime
from .credit_product_type import CreditProductType
from .interest_rate_product_type import InterestRateProductType

# Only use the forward references for type checking
CreditProductTypeRef = ForwardRef('CreditProductType')
InterestRateProductTypeRef = ForwardRef('InterestRateProductType')

class ProductType(FpMLModelBase):
    class Config:
        populate_by_field_name = True
        validate_assignment = True

    interestRate: Optional[InterestRateProductType] = Field(None)
    credit: Optional[CreditProductType] = Field(None)

# Update forward references
ProductType.update_forward_refs()
