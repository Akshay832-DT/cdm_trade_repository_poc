"""
FIX LegStrikeCurrency field (tag 942).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class LegStrikeCurrencyField(FIXFieldBase):
    """"""
    tag: str = "942"
    name: str = "LegStrikeCurrency"
    type: str = "CURRENCY"
    value: str
