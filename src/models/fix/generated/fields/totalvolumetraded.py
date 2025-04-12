
from .base import FIXFieldBase
from .types import FIXQty

class TotalVolumeTraded(FIXFieldBase):
    """FIX TotalVolumeTraded field."""
    tag: str = "387"
    name: str = "TotalVolumeTraded"
    type: str = "QTY"
    value: FIXQty
