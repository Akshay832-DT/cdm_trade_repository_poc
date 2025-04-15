"""
FIX LowPx field (tag 333).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class LowPxField(FIXFieldBase):
    """"""
    tag: str = "333"
    name: str = "LowPx"
    type: str = "PRICE"
    value: float
