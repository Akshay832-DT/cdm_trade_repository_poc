"""
FIX LegCouponPaymentDate field (tag 248).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class LegCouponPaymentDateField(FIXFieldBase):
    """"""
    tag: str = "248"
    name: str = "LegCouponPaymentDate"
    type: str = "LOCALMKTDATE"
    value: date
