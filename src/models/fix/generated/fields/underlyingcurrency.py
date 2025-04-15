"""
FIX UnderlyingCurrency field (tag 318).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class UnderlyingCurrencyField(FIXFieldBase):
    """"""
    tag: str = "318"
    name: str = "UnderlyingCurrency"
    type: str = "CURRENCY"
    value: str
