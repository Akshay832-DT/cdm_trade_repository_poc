"""
FIX LegCouponRate field (tag 615).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class LegCouponRateField(FIXFieldBase):
    """"""
    tag: str = "615"
    name: str = "LegCouponRate"
    type: str = "PERCENTAGE"
    value: float
