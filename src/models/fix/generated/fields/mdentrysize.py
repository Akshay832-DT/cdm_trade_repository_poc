"""
FIX MDEntrySize field (tag 271).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class MDEntrySizeField(FIXFieldBase):
    """"""
    tag: str = "271"
    name: str = "MDEntrySize"
    type: str = "QTY"
    value: float
