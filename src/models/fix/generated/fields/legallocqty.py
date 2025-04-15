"""
FIX LegAllocQty field (tag 673).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class LegAllocQtyField(FIXFieldBase):
    """"""
    tag: str = "673"
    name: str = "LegAllocQty"
    type: str = "QTY"
    value: float
