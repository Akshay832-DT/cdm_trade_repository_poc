"""
FIX Quantity field (tag 53).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class QuantityField(FIXFieldBase):
    """"""
    tag: str = "53"
    name: str = "Quantity"
    type: str = "QTY"
    value: float
