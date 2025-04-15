"""
FIX YieldRedemptionPriceType field (tag 698).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class YieldRedemptionPriceTypeField(FIXFieldBase):
    """"""
    tag: str = "698"
    name: str = "YieldRedemptionPriceType"
    type: str = "INT"
    value: int
