"""
FIX OfferSpotRate field (tag 190).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class OfferSpotRateField(FIXFieldBase):
    """"""
    tag: str = "190"
    name: str = "OfferSpotRate"
    type: str = "PRICE"
    value: float
