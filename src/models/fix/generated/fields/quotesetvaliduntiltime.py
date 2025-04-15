"""
FIX QuoteSetValidUntilTime field (tag 367).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class QuoteSetValidUntilTimeField(FIXFieldBase):
    """"""
    tag: str = "367"
    name: str = "QuoteSetValidUntilTime"
    type: str = "UTCTIMESTAMP"
    value: datetime
