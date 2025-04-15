"""
FIX UnderlyingSettlPrice field (tag 732).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class UnderlyingSettlPriceField(FIXFieldBase):
    """"""
    tag: str = "732"
    name: str = "UnderlyingSettlPrice"
    type: str = "PRICE"
    value: float
