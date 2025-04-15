"""
FIX BidSize field (tag 134).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class BidSizeField(FIXFieldBase):
    """"""
    tag: str = "134"
    name: str = "BidSize"
    type: str = "QTY"
    value: float
