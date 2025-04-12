
from .base import FIXFieldBase
from .types import FIXPercentage

class PctAtRisk(FIXFieldBase):
    """FIX PctAtRisk field."""
    tag: str = "869"
    name: str = "PctAtRisk"
    type: str = "PERCENTAGE"
    value: FIXPercentage
