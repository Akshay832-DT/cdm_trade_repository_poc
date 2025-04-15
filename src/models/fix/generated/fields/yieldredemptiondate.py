"""
FIX YieldRedemptionDate field (tag 696).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class YieldRedemptionDateField(FIXFieldBase):
    """"""
    tag: str = "696"
    name: str = "YieldRedemptionDate"
    type: str = "LOCALMKTDATE"
    value: date
