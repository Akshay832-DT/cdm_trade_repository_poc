
from .base import FIXFieldBase
from .types import FIXPercentage

class EFPTrackingError(FIXFieldBase):
    """FIX EFPTrackingError field."""
    tag: str = "405"
    name: str = "EFPTrackingError"
    type: str = "PERCENTAGE"
    value: FIXPercentage
