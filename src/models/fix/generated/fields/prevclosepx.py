"""
FIX PrevClosePx field (tag 140).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class PrevClosePxField(FIXFieldBase):
    """"""
    tag: str = "140"
    name: str = "PrevClosePx"
    type: str = "PRICE"
    value: float
