"""
FIX OrderQty2 field (tag 192).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class OrderQty2Field(FIXFieldBase):
    """"""
    tag: str = "192"
    name: str = "OrderQty2"
    type: str = "QTY"
    value: float
