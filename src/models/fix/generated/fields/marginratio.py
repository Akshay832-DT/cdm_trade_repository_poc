
from .base import FIXFieldBase
from .types import FIXPercentage

class MarginRatio(FIXFieldBase):
    """FIX MarginRatio field."""
    tag: str = "898"
    name: str = "MarginRatio"
    type: str = "PERCENTAGE"
    value: FIXPercentage
