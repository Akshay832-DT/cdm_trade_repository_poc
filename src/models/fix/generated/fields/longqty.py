"""
FIX LongQty field (tag 704).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class LongQtyField(FIXFieldBase):
    """"""
    tag: str = "704"
    name: str = "LongQty"
    type: str = "QTY"
    value: float
