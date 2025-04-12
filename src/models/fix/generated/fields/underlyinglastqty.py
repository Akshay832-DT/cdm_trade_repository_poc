
from .base import FIXFieldBase
from .types import FIXQty

class UnderlyingLastQty(FIXFieldBase):
    """FIX UnderlyingLastQty field."""
    tag: str = "652"
    name: str = "UnderlyingLastQty"
    type: str = "QTY"
    value: FIXQty
