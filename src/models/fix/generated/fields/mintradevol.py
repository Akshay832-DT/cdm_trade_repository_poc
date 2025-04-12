
from .base import FIXFieldBase
from .types import FIXQty

class MinTradeVol(FIXFieldBase):
    """FIX MinTradeVol field."""
    tag: str = "562"
    name: str = "MinTradeVol"
    type: str = "QTY"
    value: FIXQty
