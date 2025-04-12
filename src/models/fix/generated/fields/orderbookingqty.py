
from .base import FIXFieldBase
from .types import FIXQty

class OrderBookingQty(FIXFieldBase):
    """FIX OrderBookingQty field."""
    tag: str = "800"
    name: str = "OrderBookingQty"
    type: str = "QTY"
    value: FIXQty
