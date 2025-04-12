
from .base import FIXFieldBase
from .types import FIXPrice

class LowPx(FIXFieldBase):
    """FIX LowPx field."""
    tag: str = "333"
    name: str = "LowPx"
    type: str = "PRICE"
    value: FIXPrice
