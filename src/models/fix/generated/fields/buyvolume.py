
from .base import FIXFieldBase
from .types import FIXQty

class BuyVolume(FIXFieldBase):
    """FIX BuyVolume field."""
    tag: str = "330"
    name: str = "BuyVolume"
    type: str = "QTY"
    value: FIXQty
