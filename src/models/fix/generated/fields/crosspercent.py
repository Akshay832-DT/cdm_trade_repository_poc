
from .base import FIXFieldBase
from .types import FIXPercentage

class CrossPercent(FIXFieldBase):
    """FIX CrossPercent field."""
    tag: str = "413"
    name: str = "CrossPercent"
    type: str = "PERCENTAGE"
    value: FIXPercentage
