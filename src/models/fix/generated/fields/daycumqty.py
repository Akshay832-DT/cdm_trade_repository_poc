
from .base import FIXFieldBase
from .types import FIXQty

class DayCumQty(FIXFieldBase):
    """FIX DayCumQty field."""
    tag: str = "425"
    name: str = "DayCumQty"
    type: str = "QTY"
    value: FIXQty
