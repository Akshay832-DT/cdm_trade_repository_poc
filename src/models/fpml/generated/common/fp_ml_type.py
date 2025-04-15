"""
FpML Complex Type - FpMLType
"""

from typing import List, Optional, Any, Dict, ForwardRef, TYPE_CHECKING
from pydantic import Field
from datetime import date, datetime, time
from ..base import FpMLModelBase

# Import directly for use at runtime
from .trade_type import TradeType

# Only use the forward references for type checking
TradeTypeRef = ForwardRef('TradeType')

class FpMLType(FpMLModelBase):
    class Config:
        populate_by_field_name = True
        validate_assignment = True

    trade: TradeType = Field()

# Update forward references
FpMLType.update_forward_refs()
