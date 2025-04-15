"""
FIX UnderlyingQty field (tag 879).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class UnderlyingQtyField(FIXFieldBase):
    """"""
    tag: str = "879"
    name: str = "UnderlyingQty"
    type: str = "QTY"
    value: float
