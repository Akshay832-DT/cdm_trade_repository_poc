"""
FpML Complex Type - InterestRateProductType
"""

from typing import List, Optional, Any, Dict, ForwardRef, TYPE_CHECKING
from pydantic import Field
from datetime import date, datetime, time
from ..base import FpMLModelBase

# Import directly for use at runtime
from .swap_stream_type import SwapStreamType

# Only use the forward references for type checking
SwapStreamTypeRef = ForwardRef('SwapStreamType')

class InterestRateProductType(FpMLModelBase):
    class Config:
        populate_by_field_name = True
        validate_assignment = True

    swapStream: List[SwapStreamType] = Field()

# Update forward references
InterestRateProductType.update_forward_refs()
