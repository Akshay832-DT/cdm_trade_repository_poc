
from .base import FIXFieldBase
from .types import FIXInt

class AvgPxPrecision(FIXFieldBase):
    """FIX AvgPxPrecision field."""
    tag: str = "74"
    name: str = "AvgPxPrecision"
    type: str = "INT"
    value: FIXInt
