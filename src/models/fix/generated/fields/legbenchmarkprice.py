"""
FIX LegBenchmarkPrice field (tag 679).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class LegBenchmarkPriceField(FIXFieldBase):
    """"""
    tag: str = "679"
    name: str = "LegBenchmarkPrice"
    type: str = "PRICE"
    value: float
