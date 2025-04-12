
from .base import FIXFieldBase
from .types import FIXPercentage

class OrderPercent(FIXFieldBase):
    """FIX OrderPercent field."""
    tag: str = "516"
    name: str = "OrderPercent"
    type: str = "PERCENTAGE"
    value: FIXPercentage
