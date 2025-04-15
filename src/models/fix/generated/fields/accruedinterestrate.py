"""
FIX AccruedInterestRate field (tag 158).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class AccruedInterestRateField(FIXFieldBase):
    """"""
    tag: str = "158"
    name: str = "AccruedInterestRate"
    type: str = "PERCENTAGE"
    value: float
