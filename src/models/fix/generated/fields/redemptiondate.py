"""
FIX RedemptionDate field (tag 240).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class RedemptionDateField(FIXFieldBase):
    """"""
    tag: str = "240"
    name: str = "RedemptionDate"
    type: str = "LOCALMKTDATE"
    value: date
