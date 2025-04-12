
from .base import FIXFieldBase
from .types import FIXQty

class MinQty(FIXFieldBase):
    """FIX MinQty field."""
    tag: str = "110"
    name: str = "MinQty"
    type: str = "QTY"
    value: FIXQty
