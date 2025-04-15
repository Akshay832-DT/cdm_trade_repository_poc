"""
FIX AllocSettlCurrency field (tag 736).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class AllocSettlCurrencyField(FIXFieldBase):
    """"""
    tag: str = "736"
    name: str = "AllocSettlCurrency"
    type: str = "CURRENCY"
    value: str
