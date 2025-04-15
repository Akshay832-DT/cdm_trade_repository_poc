"""
FIX CommCurrency field (tag 479).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class CommCurrencyField(FIXFieldBase):
    """"""
    tag: str = "479"
    name: str = "CommCurrency"
    type: str = "CURRENCY"
    value: str
