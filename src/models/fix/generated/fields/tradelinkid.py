"""
FIX TradeLinkID field (tag 820).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class TradeLinkIDField(FIXFieldBase):
    """"""
    tag: str = "820"
    name: str = "TradeLinkID"
    type: str = "STRING"
    value: str
