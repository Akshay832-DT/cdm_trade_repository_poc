"""
FpML Complex Type - TradeType
"""

from typing import List, Optional, Any, Dict, ForwardRef, TYPE_CHECKING
from pydantic import Field
from datetime import date, datetime, time
from ..base import FpMLModelBase

# Import directly for use at runtime
from .product_type import ProductType
from .trade_header_type import TradeHeaderType

# Only use the forward references for type checking
ProductTypeRef = ForwardRef('ProductType')
TradeHeaderTypeRef = ForwardRef('TradeHeaderType')

class TradeType(FpMLModelBase):
    class Config:
        populate_by_field_name = True
        validate_assignment = True

    tradeHeader: TradeHeaderType = Field()
    product: ProductType = Field()

# Update forward references
TradeType.update_forward_refs()
