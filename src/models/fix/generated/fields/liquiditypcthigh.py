"""
FIX LiquidityPctHigh field (tag 403).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class LiquidityPctHighField(FIXFieldBase):
    """"""
    tag: str = "403"
    name: str = "LiquidityPctHigh"
    type: str = "PERCENTAGE"
    value: float
