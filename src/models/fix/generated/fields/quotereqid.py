"""
FIX QuoteReqID field (tag 131).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class QuoteReqIDField(FIXFieldBase):
    """"""
    tag: str = "131"
    name: str = "QuoteReqID"
    type: str = "STRING"
    value: str
