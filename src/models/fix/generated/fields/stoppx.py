"""
FIX StopPx field (tag 99).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class StopPxField(FIXFieldBase):
    """"""
    tag: str = "99"
    name: str = "StopPx"
    type: str = "PRICE"
    value: float
