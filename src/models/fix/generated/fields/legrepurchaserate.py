
from .base import FIXFieldBase
from .types import FIXPercentage

class LegRepurchaseRate(FIXFieldBase):
    """FIX LegRepurchaseRate field."""
    tag: str = "252"
    name: str = "LegRepurchaseRate"
    type: str = "PERCENTAGE"
    value: FIXPercentage
