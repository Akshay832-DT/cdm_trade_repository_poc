"""
FIX QuoteID field (tag 117).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class QuoteIDField(FIXFieldBase):
    """"""
    tag: str = "117"
    name: str = "QuoteID"
    type: str = "STRING"
    value: str
