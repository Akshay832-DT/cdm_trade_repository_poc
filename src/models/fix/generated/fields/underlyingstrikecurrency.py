"""
FIX UnderlyingStrikeCurrency field (tag 941).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class UnderlyingStrikeCurrencyField(FIXFieldBase):
    """"""
    tag: str = "941"
    name: str = "UnderlyingStrikeCurrency"
    type: str = "CURRENCY"
    value: str
