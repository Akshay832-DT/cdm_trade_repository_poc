"""
FIX UnderlyingCouponRate field (tag 435).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class UnderlyingCouponRateField(FIXFieldBase):
    """"""
    tag: str = "435"
    name: str = "UnderlyingCouponRate"
    type: str = "PERCENTAGE"
    value: float
