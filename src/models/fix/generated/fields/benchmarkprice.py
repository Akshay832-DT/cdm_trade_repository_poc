"""
FIX BenchmarkPrice field (tag 662).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class BenchmarkPriceField(FIXFieldBase):
    """"""
    tag: str = "662"
    name: str = "BenchmarkPrice"
    type: str = "PRICE"
    value: float
