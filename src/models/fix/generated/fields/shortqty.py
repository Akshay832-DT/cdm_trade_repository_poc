
from .base import FIXFieldBase
from .types import FIXQty

class ShortQty(FIXFieldBase):
    """FIX ShortQty field."""
    tag: str = "705"
    name: str = "ShortQty"
    type: str = "QTY"
    value: FIXQty
