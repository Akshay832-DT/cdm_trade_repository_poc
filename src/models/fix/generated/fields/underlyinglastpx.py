"""
FIX UnderlyingLastPx field (tag 651).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class UnderlyingLastPxField(FIXFieldBase):
    """"""
    tag: str = "651"
    name: str = "UnderlyingLastPx"
    type: str = "PRICE"
    value: float
