
from .base import FIXFieldBase
from .types import FIXPrice

class EventPx(FIXFieldBase):
    """FIX EventPx field."""
    tag: str = "867"
    name: str = "EventPx"
    type: str = "PRICE"
    value: FIXPrice
