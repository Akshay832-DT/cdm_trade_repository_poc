"""
FIX LegBenchmarkCurvePoint field (tag 678).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class LegBenchmarkCurvePointField(FIXFieldBase):
    """"""
    tag: str = "678"
    name: str = "LegBenchmarkCurvePoint"
    type: str = "STRING"
    value: str
