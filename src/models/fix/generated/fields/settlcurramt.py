"""
FIX SettlCurrAmt field (tag 119).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class SettlCurrAmtField(FIXFieldBase):
    """"""
    tag: str = "119"
    name: str = "SettlCurrAmt"
    type: str = "AMT"
    value: float
