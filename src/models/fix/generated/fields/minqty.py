"""
FIX MinQty field (tag 110).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class MinQtyField(FIXFieldBase):
    """"""
    tag: str = "110"
    name: str = "MinQty"
    type: str = "QTY"
    value: float
