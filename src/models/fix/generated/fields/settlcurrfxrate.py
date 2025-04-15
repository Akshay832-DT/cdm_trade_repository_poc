"""
FIX SettlCurrFxRate field (tag 155).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class SettlCurrFxRateField(FIXFieldBase):
    """"""
    tag: str = "155"
    name: str = "SettlCurrFxRate"
    type: str = "FLOAT"
    value: float
