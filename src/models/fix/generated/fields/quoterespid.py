"""
FIX QuoteRespID field (tag 693).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class QuoteRespIDField(FIXFieldBase):
    """"""
    tag: str = "693"
    name: str = "QuoteRespID"
    type: str = "STRING"
    value: str
