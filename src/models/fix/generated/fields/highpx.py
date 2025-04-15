"""
FIX HighPx field (tag 332).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class HighPxField(FIXFieldBase):
    """"""
    tag: str = "332"
    name: str = "HighPx"
    type: str = "PRICE"
    value: float
