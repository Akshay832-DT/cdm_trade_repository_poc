"""
FIX LegSettlDate field (tag 588).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class LegSettlDateField(FIXFieldBase):
    """"""
    tag: str = "588"
    name: str = "LegSettlDate"
    type: str = "LOCALMKTDATE"
    value: date
