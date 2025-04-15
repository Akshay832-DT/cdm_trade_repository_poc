"""
FIX TargetStrategyPerformance field (tag 850).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class TargetStrategyPerformanceField(FIXFieldBase):
    """"""
    tag: str = "850"
    name: str = "TargetStrategyPerformance"
    type: str = "FLOAT"
    value: float
