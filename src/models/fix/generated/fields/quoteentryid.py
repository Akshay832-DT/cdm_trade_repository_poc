"""
FIX QuoteEntryID field (tag 299).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class QuoteEntryIDField(FIXFieldBase):
    """"""
    tag: str = "299"
    name: str = "QuoteEntryID"
    type: str = "STRING"
    value: str
