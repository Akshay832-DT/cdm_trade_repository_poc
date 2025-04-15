"""
FIX LegRedemptionDate field (tag 254).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class LegRedemptionDateField(FIXFieldBase):
    """"""
    tag: str = "254"
    name: str = "LegRedemptionDate"
    type: str = "LOCALMKTDATE"
    value: date
