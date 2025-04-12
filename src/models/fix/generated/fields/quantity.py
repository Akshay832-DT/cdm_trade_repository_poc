
from .base import FIXFieldBase
from .types import FIXQty

class Quantity(FIXFieldBase):
    """FIX Quantity field."""
    tag: str = "53"
    name: str = "Quantity"
    type: str = "QTY"
    value: FIXQty
