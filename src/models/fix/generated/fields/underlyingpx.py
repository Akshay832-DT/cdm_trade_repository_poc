
from .base import FIXFieldBase
from .types import FIXPrice

class UnderlyingPx(FIXFieldBase):
    """FIX UnderlyingPx field."""
    tag: str = "810"
    name: str = "UnderlyingPx"
    type: str = "PRICE"
    value: FIXPrice
