"""
FIX SettlPrice field (tag 730).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class SettlPriceField(FIXFieldBase):
    """"""
    tag: str = "730"
    name: str = "SettlPrice"
    type: str = "PRICE"
    value: float
