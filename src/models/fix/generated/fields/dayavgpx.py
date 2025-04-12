
from .base import FIXFieldBase
from .types import FIXPrice

class DayAvgPx(FIXFieldBase):
    """FIX DayAvgPx field."""
    tag: str = "426"
    name: str = "DayAvgPx"
    type: str = "PRICE"
    value: FIXPrice
