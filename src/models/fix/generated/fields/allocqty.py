
from .base import FIXFieldBase
from .types import FIXQty

class AllocQty(FIXFieldBase):
    """FIX AllocQty field."""
    tag: str = "80"
    name: str = "AllocQty"
    type: str = "QTY"
    value: FIXQty
