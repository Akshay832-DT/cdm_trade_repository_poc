"""
FIX LegStrikePrice field (tag 612).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class LegStrikePriceField(FIXFieldBase):
    """"""
    tag: str = "612"
    name: str = "LegStrikePrice"
    type: str = "PRICE"
    value: float
