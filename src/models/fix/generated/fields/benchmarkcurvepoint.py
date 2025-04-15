"""
FIX BenchmarkCurvePoint field (tag 222).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class BenchmarkCurvePointField(FIXFieldBase):
    """"""
    tag: str = "222"
    name: str = "BenchmarkCurvePoint"
    type: str = "STRING"
    value: str
