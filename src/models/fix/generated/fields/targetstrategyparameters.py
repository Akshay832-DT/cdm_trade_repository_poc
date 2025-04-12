
from .base import FIXFieldBase
from .types import FIXString

class TargetStrategyParameters(FIXFieldBase):
    """FIX TargetStrategyParameters field."""
    tag: str = "848"
    name: str = "TargetStrategyParameters"
    type: str = "STRING"
    value: FIXString
