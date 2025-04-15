"""
FIX OfferPx field (tag 133).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class OfferPxField(FIXFieldBase):
    """"""
    tag: str = "133"
    name: str = "OfferPx"
    type: str = "PRICE"
    value: float
