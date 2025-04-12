
from .base import FIXFieldBase
from .types import FIXPercentage

class DistribPercentage(FIXFieldBase):
    """FIX DistribPercentage field."""
    tag: str = "512"
    name: str = "DistribPercentage"
    type: str = "PERCENTAGE"
    value: FIXPercentage
