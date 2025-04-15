"""
FIX NoExecs field (tag 124).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class NoExecsField(FIXFieldBase):
    """"""
    tag: str = "124"
    name: str = "NoExecs"
    type: str = "NUMINGROUP"
    value: int
