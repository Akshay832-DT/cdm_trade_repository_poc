"""
FIX AvgPx field (tag 6).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class AvgPxField(FIXFieldBase):
    """"""
    tag: str = "6"
    name: str = "AvgPx"
    type: str = "PRICE"
    value: float
