"""
FIX UnderlyingPx field (tag 810).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class UnderlyingPxField(FIXFieldBase):
    """"""
    tag: str = "810"
    name: str = "UnderlyingPx"
    type: str = "PRICE"
    value: float
