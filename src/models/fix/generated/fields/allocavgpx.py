
from .base import FIXFieldBase
from .types import FIXPrice

class AllocAvgPx(FIXFieldBase):
    """FIX AllocAvgPx field."""
    tag: str = "153"
    name: str = "AllocAvgPx"
    type: str = "PRICE"
    value: FIXPrice
