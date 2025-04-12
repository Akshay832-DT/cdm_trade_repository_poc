
from .base import FIXFieldBase
from .types import FIXPrice

class LastPx(FIXFieldBase):
    """FIX LastPx field."""
    tag: str = "31"
    name: str = "LastPx"
    type: str = "PRICE"
    value: FIXPrice
