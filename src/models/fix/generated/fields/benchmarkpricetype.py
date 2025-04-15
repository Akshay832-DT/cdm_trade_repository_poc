"""
FIX BenchmarkPriceType field (tag 663).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class BenchmarkPriceTypeField(FIXFieldBase):
    """"""
    tag: str = "663"
    name: str = "BenchmarkPriceType"
    type: str = "INT"
    value: int
