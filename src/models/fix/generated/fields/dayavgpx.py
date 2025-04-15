"""
FIX DayAvgPx field (tag 426).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class DayAvgPxField(FIXFieldBase):
    """"""
    tag: str = "426"
    name: str = "DayAvgPx"
    type: str = "PRICE"
    value: float
