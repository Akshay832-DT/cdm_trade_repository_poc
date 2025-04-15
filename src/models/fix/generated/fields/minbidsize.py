"""
FIX MinBidSize field (tag 647).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class MinBidSizeField(FIXFieldBase):
    """"""
    tag: str = "647"
    name: str = "MinBidSize"
    type: str = "QTY"
    value: float
