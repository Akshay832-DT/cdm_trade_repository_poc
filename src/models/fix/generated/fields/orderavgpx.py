
from .base import FIXFieldBase
from .types import FIXPrice

class OrderAvgPx(FIXFieldBase):
    """FIX OrderAvgPx field."""
    tag: str = "799"
    name: str = "OrderAvgPx"
    type: str = "PRICE"
    value: FIXPrice
