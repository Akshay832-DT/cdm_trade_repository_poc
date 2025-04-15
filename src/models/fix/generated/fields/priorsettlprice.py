"""
FIX PriorSettlPrice field (tag 734).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class PriorSettlPriceField(FIXFieldBase):
    """"""
    tag: str = "734"
    name: str = "PriorSettlPrice"
    type: str = "PRICE"
    value: float
