"""
FIX LegPrice field (tag 566).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class LegPriceField(FIXFieldBase):
    """"""
    tag: str = "566"
    name: str = "LegPrice"
    type: str = "PRICE"
    value: float
