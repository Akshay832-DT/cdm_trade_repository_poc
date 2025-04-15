"""
FIX OrderPercent field (tag 516).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class OrderPercentField(FIXFieldBase):
    """"""
    tag: str = "516"
    name: str = "OrderPercent"
    type: str = "PERCENTAGE"
    value: float
