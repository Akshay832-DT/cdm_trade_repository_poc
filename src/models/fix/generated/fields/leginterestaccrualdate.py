"""
FIX LegInterestAccrualDate field (tag 956).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class LegInterestAccrualDateField(FIXFieldBase):
    """"""
    tag: str = "956"
    name: str = "LegInterestAccrualDate"
    type: str = "LOCALMKTDATE"
    value: date
