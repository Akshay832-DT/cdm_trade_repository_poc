"""
FIX NoQuoteEntries field (tag 295).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class NoQuoteEntriesField(FIXFieldBase):
    """"""
    tag: str = "295"
    name: str = "NoQuoteEntries"
    type: str = "NUMINGROUP"
    value: int
