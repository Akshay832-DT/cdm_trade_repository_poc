"""
FIX UnderlyingEndPrice field (tag 883).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class UnderlyingEndPriceField(FIXFieldBase):
    """"""
    tag: str = "883"
    name: str = "UnderlyingEndPrice"
    type: str = "PRICE"
    value: float
