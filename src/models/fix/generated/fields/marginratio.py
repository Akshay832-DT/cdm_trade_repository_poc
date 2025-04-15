"""
FIX MarginRatio field (tag 898).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class MarginRatioField(FIXFieldBase):
    """"""
    tag: str = "898"
    name: str = "MarginRatio"
    type: str = "PERCENTAGE"
    value: float
