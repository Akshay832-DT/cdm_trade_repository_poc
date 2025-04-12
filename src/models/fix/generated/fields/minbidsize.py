
from .base import FIXFieldBase
from .types import FIXQty

class MinBidSize(FIXFieldBase):
    """FIX MinBidSize field."""
    tag: str = "647"
    name: str = "MinBidSize"
    type: str = "QTY"
    value: FIXQty
