"""
FIX UnderlyingRepurchaseRate field (tag 245).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class UnderlyingRepurchaseRateField(FIXFieldBase):
    """"""
    tag: str = "245"
    name: str = "UnderlyingRepurchaseRate"
    type: str = "PERCENTAGE"
    value: float
