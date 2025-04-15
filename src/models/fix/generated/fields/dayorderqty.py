"""
FIX DayOrderQty field (tag 424).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class DayOrderQtyField(FIXFieldBase):
    """"""
    tag: str = "424"
    name: str = "DayOrderQty"
    type: str = "QTY"
    value: float
