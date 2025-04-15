"""
FIX LastQty field (tag 32).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class LastQtyField(FIXFieldBase):
    """"""
    tag: str = "32"
    name: str = "LastQty"
    type: str = "QTY"
    value: float
