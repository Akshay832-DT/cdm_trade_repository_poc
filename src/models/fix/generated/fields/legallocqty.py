
from .base import FIXFieldBase
from .types import FIXQty

class LegAllocQty(FIXFieldBase):
    """FIX LegAllocQty field."""
    tag: str = "673"
    name: str = "LegAllocQty"
    type: str = "QTY"
    value: FIXQty
