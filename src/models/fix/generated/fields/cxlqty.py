"""
FIX CxlQty field (tag 84).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class CxlQtyField(FIXFieldBase):
    """"""
    tag: str = "84"
    name: str = "CxlQty"
    type: str = "QTY"
    value: float
