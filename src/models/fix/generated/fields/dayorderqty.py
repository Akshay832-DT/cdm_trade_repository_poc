
from .base import FIXFieldBase
from .types import FIXQty

class DayOrderQty(FIXFieldBase):
    """FIX DayOrderQty field."""
    tag: str = "424"
    name: str = "DayOrderQty"
    type: str = "QTY"
    value: FIXQty
