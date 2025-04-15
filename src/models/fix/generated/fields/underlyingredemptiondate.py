"""
FIX UnderlyingRedemptionDate field (tag 247).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class UnderlyingRedemptionDateField(FIXFieldBase):
    """"""
    tag: str = "247"
    name: str = "UnderlyingRedemptionDate"
    type: str = "LOCALMKTDATE"
    value: date
