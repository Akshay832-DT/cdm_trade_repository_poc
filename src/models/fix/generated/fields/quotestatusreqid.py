"""
FIX QuoteStatusReqID field (tag 649).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class QuoteStatusReqIDField(FIXFieldBase):
    """"""
    tag: str = "649"
    name: str = "QuoteStatusReqID"
    type: str = "STRING"
    value: str
