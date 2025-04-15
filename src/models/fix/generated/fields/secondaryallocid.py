"""
FIX SecondaryAllocID field (tag 793).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class SecondaryAllocIDField(FIXFieldBase):
    """"""
    tag: str = "793"
    name: str = "SecondaryAllocID"
    type: str = "STRING"
    value: str
