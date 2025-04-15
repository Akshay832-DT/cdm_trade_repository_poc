"""
FIX CrossPercent field (tag 413).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class CrossPercentField(FIXFieldBase):
    """"""
    tag: str = "413"
    name: str = "CrossPercent"
    type: str = "PERCENTAGE"
    value: float
