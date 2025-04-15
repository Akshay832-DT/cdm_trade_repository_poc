"""
FIX BenchmarkCurveCurrency field (tag 220).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class BenchmarkCurveCurrencyField(FIXFieldBase):
    """"""
    tag: str = "220"
    name: str = "BenchmarkCurveCurrency"
    type: str = "CURRENCY"
    value: str
