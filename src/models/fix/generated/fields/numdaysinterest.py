"""
FIX NumDaysInterest field (tag 157).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class NumDaysInterestField(FIXFieldBase):
    """"""
    tag: str = "157"
    name: str = "NumDaysInterest"
    type: str = "INT"
    value: int
