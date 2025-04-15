"""
FIX NoAltMDSource field (tag 816).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class NoAltMDSourceField(FIXFieldBase):
    """"""
    tag: str = "816"
    name: str = "NoAltMDSource"
    type: str = "NUMINGROUP"
    value: int
