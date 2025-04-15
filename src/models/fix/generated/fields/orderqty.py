"""
FIX OrderQty field (tag 38).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class OrderQtyField(FIXFieldBase):
    """"""
    tag: str = "38"
    name: str = "OrderQty"
    type: str = "QTY"
    value: float
