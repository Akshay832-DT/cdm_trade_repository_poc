
from .base import FIXFieldBase
from .types import FIXQty

class RoundLot(FIXFieldBase):
    """FIX RoundLot field."""
    tag: str = "561"
    name: str = "RoundLot"
    type: str = "QTY"
    value: FIXQty
