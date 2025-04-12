
from .base import FIXFieldBase
from .types import FIXPrice

class AvgPx(FIXFieldBase):
    """FIX AvgPx field."""
    tag: str = "6"
    name: str = "AvgPx"
    type: str = "PRICE"
    value: FIXPrice
