"""
FIX MiscFeeAmt field (tag 137).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class MiscFeeAmtField(FIXFieldBase):
    """"""
    tag: str = "137"
    name: str = "MiscFeeAmt"
    type: str = "AMT"
    value: float
