"""
FIX LegCurrency field (tag 556).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class LegCurrencyField(FIXFieldBase):
    """"""
    tag: str = "556"
    name: str = "LegCurrency"
    type: str = "CURRENCY"
    value: str
