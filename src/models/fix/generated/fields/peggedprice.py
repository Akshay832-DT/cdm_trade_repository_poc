"""
FIX PeggedPrice field (tag 839).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class PeggedPriceField(FIXFieldBase):
    """"""
    tag: str = "839"
    name: str = "PeggedPrice"
    type: str = "PRICE"
    value: float
