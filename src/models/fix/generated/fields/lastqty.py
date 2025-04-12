
from .base import FIXFieldBase
from .types import FIXQty

class LastQty(FIXFieldBase):
    """FIX LastQty field."""
    tag: str = "32"
    name: str = "LastQty"
    type: str = "QTY"
    value: FIXQty
