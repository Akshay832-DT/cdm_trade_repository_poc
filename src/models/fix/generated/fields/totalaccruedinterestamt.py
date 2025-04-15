"""
FIX TotalAccruedInterestAmt field (tag 540).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class TotalAccruedInterestAmtField(FIXFieldBase):
    """"""
    tag: str = "540"
    name: str = "TotalAccruedInterestAmt"
    type: str = "AMT"
    value: float
