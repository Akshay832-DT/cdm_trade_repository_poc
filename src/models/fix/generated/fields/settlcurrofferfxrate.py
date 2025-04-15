"""
FIX SettlCurrOfferFxRate field (tag 657).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class SettlCurrOfferFxRateField(FIXFieldBase):
    """"""
    tag: str = "657"
    name: str = "SettlCurrOfferFxRate"
    type: str = "FLOAT"
    value: float
