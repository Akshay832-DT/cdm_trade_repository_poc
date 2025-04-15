"""
FIX CashOrderQty field (tag 152).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class CashOrderQtyField(FIXFieldBase):
    """"""
    tag: str = "152"
    name: str = "CashOrderQty"
    type: str = "QTY"
    value: float
