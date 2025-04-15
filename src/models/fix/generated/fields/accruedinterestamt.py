"""
FIX AccruedInterestAmt field (tag 159).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class AccruedInterestAmtField(FIXFieldBase):
    """"""
    tag: str = "159"
    name: str = "AccruedInterestAmt"
    type: str = "AMT"
    value: float
