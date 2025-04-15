"""
FIX LegBenchmarkPriceType field (tag 680).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class LegBenchmarkPriceTypeField(FIXFieldBase):
    """"""
    tag: str = "680"
    name: str = "LegBenchmarkPriceType"
    type: str = "INT"
    value: int
