"""
FIX Spread field (tag 218).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class SpreadField(FIXFieldBase):
    """"""
    tag: str = "218"
    name: str = "Spread"
    type: str = "PRICEOFFSET"
    value: float
