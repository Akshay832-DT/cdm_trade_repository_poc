
from .base import FIXFieldBase
from .types import FIXQty

class UnderlyingQty(FIXFieldBase):
    """FIX UnderlyingQty field."""
    tag: str = "879"
    name: str = "UnderlyingQty"
    type: str = "QTY"
    value: FIXQty
