"""
FIX Currency field (tag 15).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class CurrencyField(FIXFieldBase):
    """"""
    tag: str = "15"
    name: str = "Currency"
    type: str = "CURRENCY"
    value: str
