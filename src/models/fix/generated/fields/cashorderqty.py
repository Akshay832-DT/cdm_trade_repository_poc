
from .base import FIXFieldBase
from .types import FIXQty

class CashOrderQty(FIXFieldBase):
    """FIX CashOrderQty field."""
    tag: str = "152"
    name: str = "CashOrderQty"
    type: str = "QTY"
    value: FIXQty
