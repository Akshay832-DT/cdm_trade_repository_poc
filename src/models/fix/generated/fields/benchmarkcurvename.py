"""
FIX BenchmarkCurveName field (tag 221).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class BenchmarkCurveNameField(FIXFieldBase):
    """"""
    tag: str = "221"
    name: str = "BenchmarkCurveName"
    type: str = "STRING"
    value: str
