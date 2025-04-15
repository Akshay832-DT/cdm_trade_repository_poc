"""
FIX ThresholdAmount field (tag 834).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class ThresholdAmountField(FIXFieldBase):
    """"""
    tag: str = "834"
    name: str = "ThresholdAmount"
    type: str = "PRICEOFFSET"
    value: float
