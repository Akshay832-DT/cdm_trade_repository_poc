"""
FIX StrikeCurrency field (tag 947).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class StrikeCurrencyField(FIXFieldBase):
    """"""
    tag: str = "947"
    name: str = "StrikeCurrency"
    type: str = "CURRENCY"
    value: str
