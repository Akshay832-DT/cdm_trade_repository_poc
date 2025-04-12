
from .base import FIXFieldBase
from .types import FIXQty

class OrderQty2(FIXFieldBase):
    """FIX OrderQty2 field."""
    tag: str = "192"
    name: str = "OrderQty2"
    type: str = "QTY"
    value: FIXQty
