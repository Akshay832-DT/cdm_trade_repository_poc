"""
FIX NoMDEntries field (tag 268).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class NoMDEntriesField(FIXFieldBase):
    """"""
    tag: str = "268"
    name: str = "NoMDEntries"
    type: str = "NUMINGROUP"
    value: int
