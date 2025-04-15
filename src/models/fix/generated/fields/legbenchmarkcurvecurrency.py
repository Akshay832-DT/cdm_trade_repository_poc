"""
FIX LegBenchmarkCurveCurrency field (tag 676).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class LegBenchmarkCurveCurrencyField(FIXFieldBase):
    """"""
    tag: str = "676"
    name: str = "LegBenchmarkCurveCurrency"
    type: str = "CURRENCY"
    value: str
