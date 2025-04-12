
from .base import FIXFieldBase
from .types import FIXQty

class OrderCapacityQty(FIXFieldBase):
    """FIX OrderCapacityQty field."""
    tag: str = "863"
    name: str = "OrderCapacityQty"
    type: str = "QTY"
    value: FIXQty
