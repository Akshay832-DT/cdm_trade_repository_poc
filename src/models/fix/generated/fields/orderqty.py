
from .base import FIXFieldBase
from .types import FIXQty

class OrderQty(FIXFieldBase):
    """FIX OrderQty field."""
    tag: str = "38"
    name: str = "OrderQty"
    type: str = "QTY"
    value: FIXQty
