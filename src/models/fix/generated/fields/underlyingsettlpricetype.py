"""
FIX UnderlyingSettlPriceType field (tag 733).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class UnderlyingSettlPriceTypeField(FIXFieldBase):
    """"""
    tag: str = "733"
    name: str = "UnderlyingSettlPriceType"
    type: str = "INT"
    value: int
