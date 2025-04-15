"""
FIX OfferForwardPoints field (tag 191).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class OfferForwardPointsField(FIXFieldBase):
    """"""
    tag: str = "191"
    name: str = "OfferForwardPoints"
    type: str = "PRICEOFFSET"
    value: float
