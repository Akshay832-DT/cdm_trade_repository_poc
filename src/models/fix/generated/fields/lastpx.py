"""
FIX LastPx field (tag 31).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class LastPxField(FIXFieldBase):
    """"""
    tag: str = "31"
    name: str = "LastPx"
    type: str = "PRICE"
    value: float
