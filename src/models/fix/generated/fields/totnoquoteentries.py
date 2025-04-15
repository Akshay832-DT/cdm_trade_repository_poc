"""
FIX TotNoQuoteEntries field (tag 304).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class TotNoQuoteEntriesField(FIXFieldBase):
    """"""
    tag: str = "304"
    name: str = "TotNoQuoteEntries"
    type: str = "INT"
    value: int
