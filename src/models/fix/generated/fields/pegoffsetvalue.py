"""
FIX PegOffsetValue field (tag 211).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class PegOffsetValueField(FIXFieldBase):
    """"""
    tag: str = "211"
    name: str = "PegOffsetValue"
    type: str = "FLOAT"
    value: float
