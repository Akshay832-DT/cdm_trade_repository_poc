"""
FIX RawDataLength field (tag 95).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class RawDataLengthField(FIXFieldBase):
    """"""
    tag: str = "95"
    name: str = "RawDataLength"
    type: str = "LENGTH"
    value: int
