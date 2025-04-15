"""
FIX AllocAvgPx field (tag 153).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class AllocAvgPxField(FIXFieldBase):
    """"""
    tag: str = "153"
    name: str = "AllocAvgPx"
    type: str = "PRICE"
    value: float
