
from .base import FIXFieldBase
from .types import FIXQty

class LeavesQty(FIXFieldBase):
    """FIX LeavesQty field."""
    tag: str = "151"
    name: str = "LeavesQty"
    type: str = "QTY"
    value: FIXQty
