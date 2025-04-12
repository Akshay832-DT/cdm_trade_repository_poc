
from .base import FIXFieldBase
from .types import FIXQty

class BidSize(FIXFieldBase):
    """FIX BidSize field."""
    tag: str = "134"
    name: str = "BidSize"
    type: str = "QTY"
    value: FIXQty
