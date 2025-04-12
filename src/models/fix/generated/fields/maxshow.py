
from .base import FIXFieldBase
from .types import FIXQty

class MaxShow(FIXFieldBase):
    """FIX MaxShow field."""
    tag: str = "210"
    name: str = "MaxShow"
    type: str = "QTY"
    value: FIXQty
