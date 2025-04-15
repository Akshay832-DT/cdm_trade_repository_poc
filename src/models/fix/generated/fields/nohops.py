"""
FIX NoHops field (tag 627).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class NoHopsField(FIXFieldBase):
    """"""
    tag: str = "627"
    name: str = "NoHops"
    type: str = "NUMINGROUP"
    value: int
