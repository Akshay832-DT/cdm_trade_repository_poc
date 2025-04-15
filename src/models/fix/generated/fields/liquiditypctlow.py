"""
FIX LiquidityPctLow field (tag 402).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class LiquidityPctLowField(FIXFieldBase):
    """"""
    tag: str = "402"
    name: str = "LiquidityPctLow"
    type: str = "PERCENTAGE"
    value: float
