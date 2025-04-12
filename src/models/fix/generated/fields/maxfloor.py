
from .base import FIXFieldBase
from .types import FIXQty

class MaxFloor(FIXFieldBase):
    """FIX MaxFloor field."""
    tag: str = "111"
    name: str = "MaxFloor"
    type: str = "QTY"
    value: FIXQty
