"""
FIX GrossTradeAmt field (tag 381).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class GrossTradeAmtField(FIXFieldBase):
    """"""
    tag: str = "381"
    name: str = "GrossTradeAmt"
    type: str = "AMT"
    value: float
