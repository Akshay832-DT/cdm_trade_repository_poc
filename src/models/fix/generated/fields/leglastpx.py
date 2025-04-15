"""
FIX LegLastPx field (tag 637).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class LegLastPxField(FIXFieldBase):
    """"""
    tag: str = "637"
    name: str = "LegLastPx"
    type: str = "PRICE"
    value: float
