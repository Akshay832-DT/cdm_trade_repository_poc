"""
FIX UnderlyingLastQty field (tag 652).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class UnderlyingLastQtyField(FIXFieldBase):
    """"""
    tag: str = "652"
    name: str = "UnderlyingLastQty"
    type: str = "QTY"
    value: float
