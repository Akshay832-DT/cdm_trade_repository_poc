"""
FIX BidForwardPoints2 field (tag 642).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class BidForwardPoints2Field(FIXFieldBase):
    """"""
    tag: str = "642"
    name: str = "BidForwardPoints2"
    type: str = "PRICEOFFSET"
    value: float
