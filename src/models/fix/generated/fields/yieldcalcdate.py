"""
FIX YieldCalcDate field (tag 701).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class YieldCalcDateField(FIXFieldBase):
    """"""
    tag: str = "701"
    name: str = "YieldCalcDate"
    type: str = "LOCALMKTDATE"
    value: date
