
from .base import FIXFieldBase
from .types import FIXPercentage

class UnderlyingRepurchaseRate(FIXFieldBase):
    """FIX UnderlyingRepurchaseRate field."""
    tag: str = "245"
    name: str = "UnderlyingRepurchaseRate"
    type: str = "PERCENTAGE"
    value: FIXPercentage
