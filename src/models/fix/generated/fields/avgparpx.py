
from .base import FIXFieldBase
from .types import FIXPrice

class AvgParPx(FIXFieldBase):
    """FIX AvgParPx field."""
    tag: str = "860"
    name: str = "AvgParPx"
    type: str = "PRICE"
    value: FIXPrice
