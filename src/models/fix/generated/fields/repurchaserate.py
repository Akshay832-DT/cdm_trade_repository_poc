
from .base import FIXFieldBase
from .types import FIXPercentage

class RepurchaseRate(FIXFieldBase):
    """FIX RepurchaseRate field."""
    tag: str = "227"
    name: str = "RepurchaseRate"
    type: str = "PERCENTAGE"
    value: FIXPercentage
