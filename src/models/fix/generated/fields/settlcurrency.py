"""
FIX SettlCurrency field (tag 120).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class SettlCurrencyField(FIXFieldBase):
    """"""
    tag: str = "120"
    name: str = "SettlCurrency"
    type: str = "CURRENCY"
    value: str
