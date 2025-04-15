"""
FIX AllocAccruedInterestAmt field (tag 742).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class AllocAccruedInterestAmtField(FIXFieldBase):
    """"""
    tag: str = "742"
    name: str = "AllocAccruedInterestAmt"
    type: str = "AMT"
    value: float
