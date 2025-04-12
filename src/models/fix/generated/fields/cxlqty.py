
from .base import FIXFieldBase
from .types import FIXQty

class CxlQty(FIXFieldBase):
    """FIX CxlQty field."""
    tag: str = "84"
    name: str = "CxlQty"
    type: str = "QTY"
    value: FIXQty
