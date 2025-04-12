
from .base import FIXFieldBase
from .types import FIXString

class ThresholdAmount(FIXFieldBase):
    """FIX ThresholdAmount field."""
    tag: str = "834"
    name: str = "ThresholdAmount"
    type: str = "PRICEOFFSET"
    value: FIXString
