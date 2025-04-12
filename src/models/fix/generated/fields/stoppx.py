
from .base import FIXFieldBase
from .types import FIXPrice

class StopPx(FIXFieldBase):
    """FIX StopPx field."""
    tag: str = "99"
    name: str = "StopPx"
    type: str = "PRICE"
    value: FIXPrice
