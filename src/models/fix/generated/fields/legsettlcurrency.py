"""
FIX LegSettlCurrency field (tag 675).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class LegSettlCurrencyField(FIXFieldBase):
    """"""
    tag: str = "675"
    name: str = "LegSettlCurrency"
    type: str = "CURRENCY"
    value: str
