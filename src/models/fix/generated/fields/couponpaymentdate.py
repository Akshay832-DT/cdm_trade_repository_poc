"""
FIX CouponPaymentDate field (tag 224).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class CouponPaymentDateField(FIXFieldBase):
    """"""
    tag: str = "224"
    name: str = "CouponPaymentDate"
    type: str = "LOCALMKTDATE"
    value: date
