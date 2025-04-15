"""
FIX QuoteSetID field (tag 302).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class QuoteSetIDField(FIXFieldBase):
    """"""
    tag: str = "302"
    name: str = "QuoteSetID"
    type: str = "STRING"
    value: str
