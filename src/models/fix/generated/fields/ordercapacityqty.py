"""
FIX OrderCapacityQty field (tag 863).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class OrderCapacityQtyField(FIXFieldBase):
    """"""
    tag: str = "863"
    name: str = "OrderCapacityQty"
    type: str = "QTY"
    value: float
