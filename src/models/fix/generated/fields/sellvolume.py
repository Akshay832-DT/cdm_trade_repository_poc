
from .base import FIXFieldBase
from .types import FIXQty

class SellVolume(FIXFieldBase):
    """FIX SellVolume field."""
    tag: str = "331"
    name: str = "SellVolume"
    type: str = "QTY"
    value: FIXQty
