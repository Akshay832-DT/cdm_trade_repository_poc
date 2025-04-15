"""
FIX DayCumQty field (tag 425).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class DayCumQtyField(FIXFieldBase):
    """"""
    tag: str = "425"
    name: str = "DayCumQty"
    type: str = "QTY"
    value: float
