
from .base import FIXFieldBase
from .types import FIXFloat

class TargetStrategyPerformance(FIXFieldBase):
    """FIX TargetStrategyPerformance field."""
    tag: str = "850"
    name: str = "TargetStrategyPerformance"
    type: str = "FLOAT"
    value: FIXFloat
