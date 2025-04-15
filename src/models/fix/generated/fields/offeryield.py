"""
FIX OfferYield field (tag 634).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class OfferYieldField(FIXFieldBase):
    """"""
    tag: str = "634"
    name: str = "OfferYield"
    type: str = "PERCENTAGE"
    value: float
