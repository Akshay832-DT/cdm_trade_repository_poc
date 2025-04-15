"""
FIX AllocQty field (tag 80).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class AllocQtyField(FIXFieldBase):
    """"""
    tag: str = "80"
    name: str = "AllocQty"
    type: str = "QTY"
    value: float
