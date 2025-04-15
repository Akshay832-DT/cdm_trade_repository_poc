"""
FIX SettlCurrBidFxRate field (tag 656).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class SettlCurrBidFxRateField(FIXFieldBase):
    """"""
    tag: str = "656"
    name: str = "SettlCurrBidFxRate"
    type: str = "FLOAT"
    value: float
