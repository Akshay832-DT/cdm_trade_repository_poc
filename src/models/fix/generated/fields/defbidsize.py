
from .base import FIXFieldBase
from .types import FIXQty

class DefBidSize(FIXFieldBase):
    """FIX DefBidSize field."""
    tag: str = "293"
    name: str = "DefBidSize"
    type: str = "QTY"
    value: FIXQty
