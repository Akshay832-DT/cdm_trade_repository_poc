"""
FIX BidSpotRate field (tag 188).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class BidSpotRateField(FIXFieldBase):
    """"""
    tag: str = "188"
    name: str = "BidSpotRate"
    type: str = "PRICE"
    value: float
