"""
FIX UnderlyingStrikePrice field (tag 316).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class UnderlyingStrikePriceField(FIXFieldBase):
    """"""
    tag: str = "316"
    name: str = "UnderlyingStrikePrice"
    type: str = "PRICE"
    value: float
