"""
FIX BidForwardPoints field (tag 189).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class BidForwardPointsField(FIXFieldBase):
    """"""
    tag: str = "189"
    name: str = "BidForwardPoints"
    type: str = "PRICEOFFSET"
    value: float
