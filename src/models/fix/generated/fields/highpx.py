
from .base import FIXFieldBase
from .types import FIXPrice

class HighPx(FIXFieldBase):
    """FIX HighPx field."""
    tag: str = "332"
    name: str = "HighPx"
    type: str = "PRICE"
    value: FIXPrice
