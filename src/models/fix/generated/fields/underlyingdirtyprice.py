"""
FIX UnderlyingDirtyPrice field (tag 882).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class UnderlyingDirtyPriceField(FIXFieldBase):
    """"""
    tag: str = "882"
    name: str = "UnderlyingDirtyPrice"
    type: str = "PRICE"
    value: float
