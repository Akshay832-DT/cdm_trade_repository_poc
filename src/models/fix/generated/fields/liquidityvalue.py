"""
FIX LiquidityValue field (tag 404).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class LiquidityValueField(FIXFieldBase):
    """"""
    tag: str = "404"
    name: str = "LiquidityValue"
    type: str = "AMT"
    value: float
