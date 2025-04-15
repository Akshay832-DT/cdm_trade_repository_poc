"""
FIX LegRepurchaseRate field (tag 252).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class LegRepurchaseRateField(FIXFieldBase):
    """"""
    tag: str = "252"
    name: str = "LegRepurchaseRate"
    type: str = "PERCENTAGE"
    value: float
