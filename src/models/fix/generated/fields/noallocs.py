"""
FIX NoAllocs field (tag 78).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class NoAllocsField(FIXFieldBase):
    """"""
    tag: str = "78"
    name: str = "NoAllocs"
    type: str = "NUMINGROUP"
    value: int
