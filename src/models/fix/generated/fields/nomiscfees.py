"""
FIX NoMiscFees field (tag 136).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class NoMiscFeesField(FIXFieldBase):
    """"""
    tag: str = "136"
    name: str = "NoMiscFees"
    type: str = "NUMINGROUP"
    value: int
