"""
FIX EndAccruedInterestAmt field (tag 920).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class EndAccruedInterestAmtField(FIXFieldBase):
    """"""
    tag: str = "920"
    name: str = "EndAccruedInterestAmt"
    type: str = "AMT"
    value: float
