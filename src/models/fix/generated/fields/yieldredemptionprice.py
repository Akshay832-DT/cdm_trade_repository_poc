"""
FIX YieldRedemptionPrice field (tag 697).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class YieldRedemptionPriceField(FIXFieldBase):
    """"""
    tag: str = "697"
    name: str = "YieldRedemptionPrice"
    type: str = "PRICE"
    value: float
