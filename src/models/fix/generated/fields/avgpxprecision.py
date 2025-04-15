"""
FIX AvgPxPrecision field (tag 74).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class AvgPxPrecisionField(FIXFieldBase):
    """"""
    tag: str = "74"
    name: str = "AvgPxPrecision"
    type: str = "INT"
    value: int
