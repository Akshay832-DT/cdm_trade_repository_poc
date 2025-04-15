"""
FIX NoLegAllocs field (tag 670).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class NoLegAllocsField(FIXFieldBase):
    """"""
    tag: str = "670"
    name: str = "NoLegAllocs"
    type: str = "NUMINGROUP"
    value: int
