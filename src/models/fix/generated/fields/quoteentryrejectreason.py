"""
FIX QuoteEntryRejectReason field (tag 368).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class QuoteEntryRejectReasonField(FIXFieldBase):
    """"""
    tag: str = "368"
    name: str = "QuoteEntryRejectReason"
    type: str = "INT"
    value: int
