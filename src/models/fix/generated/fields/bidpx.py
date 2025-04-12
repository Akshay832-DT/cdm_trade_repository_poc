
from .base import FIXFieldBase
from .types import FIXPrice

class BidPx(FIXFieldBase):
    """FIX BidPx field."""
    tag: str = "132"
    name: str = "BidPx"
    type: str = "PRICE"
    value: FIXPrice
