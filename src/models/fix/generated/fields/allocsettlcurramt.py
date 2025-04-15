"""
FIX AllocSettlCurrAmt field (tag 737).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class AllocSettlCurrAmtField(FIXFieldBase):
    """"""
    tag: str = "737"
    name: str = "AllocSettlCurrAmt"
    type: str = "AMT"
    value: float
