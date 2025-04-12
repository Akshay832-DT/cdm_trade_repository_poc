
from .base import FIXFieldBase
from .types import FIXString

class OrderID(FIXFieldBase):
    """FIX OrderID field."""
    tag: str = "37"
    name: str = "OrderID"
    type: str = "STRING"
    value: FIXString
