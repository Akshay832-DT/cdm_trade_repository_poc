"""
FIX ShortQty field (tag 705).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class ShortQtyField(FIXFieldBase):
    """"""
    tag: str = "705"
    name: str = "ShortQty"
    type: str = "QTY"
    value: float
