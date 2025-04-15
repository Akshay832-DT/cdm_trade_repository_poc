"""
FIX UnderlyingCouponPaymentDate field (tag 241).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class UnderlyingCouponPaymentDateField(FIXFieldBase):
    """"""
    tag: str = "241"
    name: str = "UnderlyingCouponPaymentDate"
    type: str = "LOCALMKTDATE"
    value: date
