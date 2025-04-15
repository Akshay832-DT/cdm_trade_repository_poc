"""
FIX MaxFloor field (tag 111).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class MaxFloorField(FIXFieldBase):
    """"""
    tag: str = "111"
    name: str = "MaxFloor"
    type: str = "QTY"
    value: float
