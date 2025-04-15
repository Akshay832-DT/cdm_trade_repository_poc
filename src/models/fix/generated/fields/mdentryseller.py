"""
FIX MDEntrySeller field (tag 289).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class MDEntrySellerField(FIXFieldBase):
    """"""
    tag: str = "289"
    name: str = "MDEntrySeller"
    type: str = "STRING"
    value: str
