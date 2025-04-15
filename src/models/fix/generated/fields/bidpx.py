"""
FIX BidPx field (tag 132).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class BidPxField(FIXFieldBase):
    """"""
    tag: str = "132"
    name: str = "BidPx"
    type: str = "PRICE"
    value: float
