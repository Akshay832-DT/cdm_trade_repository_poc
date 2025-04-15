"""
FIX LegBenchmarkCurveName field (tag 677).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class LegBenchmarkCurveNameField(FIXFieldBase):
    """"""
    tag: str = "677"
    name: str = "LegBenchmarkCurveName"
    type: str = "STRING"
    value: str
