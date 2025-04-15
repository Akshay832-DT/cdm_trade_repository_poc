"""
FIX CumQty field (tag 14).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class CumQtyField(FIXFieldBase):
    """"""
    tag: str = "14"
    name: str = "CumQty"
    type: str = "QTY"
    value: float
