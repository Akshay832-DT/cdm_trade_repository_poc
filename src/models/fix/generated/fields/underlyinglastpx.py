
from .base import FIXFieldBase
from .types import FIXPrice

class UnderlyingLastPx(FIXFieldBase):
    """FIX UnderlyingLastPx field."""
    tag: str = "651"
    name: str = "UnderlyingLastPx"
    type: str = "PRICE"
    value: FIXPrice
