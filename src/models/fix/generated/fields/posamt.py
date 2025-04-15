"""
FIX PosAmt field (tag 708).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class PosAmtField(FIXFieldBase):
    """"""
    tag: str = "708"
    name: str = "PosAmt"
    type: str = "AMT"
    value: float
