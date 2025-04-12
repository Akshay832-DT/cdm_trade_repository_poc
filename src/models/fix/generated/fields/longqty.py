
from .base import FIXFieldBase
from .types import FIXQty

class LongQty(FIXFieldBase):
    """FIX LongQty field."""
    tag: str = "704"
    name: str = "LongQty"
    type: str = "QTY"
    value: FIXQty
