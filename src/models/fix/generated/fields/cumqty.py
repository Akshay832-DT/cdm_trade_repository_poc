
from .base import FIXFieldBase
from .types import FIXQty

class CumQty(FIXFieldBase):
    """FIX CumQty field."""
    tag: str = "14"
    name: str = "CumQty"
    type: str = "QTY"
    value: FIXQty
