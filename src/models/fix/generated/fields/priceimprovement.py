"""
FIX PriceImprovement field (tag 639).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class PriceImprovementField(FIXFieldBase):
    """"""
    tag: str = "639"
    name: str = "PriceImprovement"
    type: str = "PRICEOFFSET"
    value: float
