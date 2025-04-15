"""
FIX MDEntryID field (tag 278).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class MDEntryIDField(FIXFieldBase):
    """"""
    tag: str = "278"
    name: str = "MDEntryID"
    type: str = "STRING"
    value: str
