"""
FIX LeavesQty field (tag 151).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class LeavesQtyField(FIXFieldBase):
    """"""
    tag: str = "151"
    name: str = "LeavesQty"
    type: str = "QTY"
    value: float
