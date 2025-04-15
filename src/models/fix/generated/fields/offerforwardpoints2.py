"""
FIX OfferForwardPoints2 field (tag 643).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class OfferForwardPoints2Field(FIXFieldBase):
    """"""
    tag: str = "643"
    name: str = "OfferForwardPoints2"
    type: str = "PRICEOFFSET"
    value: float
