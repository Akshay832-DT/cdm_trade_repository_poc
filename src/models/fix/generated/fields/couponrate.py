"""
FIX CouponRate field (tag 223).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class CouponRateField(FIXFieldBase):
    """"""
    tag: str = "223"
    name: str = "CouponRate"
    type: str = "PERCENTAGE"
    value: float
