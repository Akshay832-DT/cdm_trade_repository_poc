"""
FIX MinTradeVol field (tag 562).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class MinTradeVolField(FIXFieldBase):
    """"""
    tag: str = "562"
    name: str = "MinTradeVol"
    type: str = "QTY"
    value: float
