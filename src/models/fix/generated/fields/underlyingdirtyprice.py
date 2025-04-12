
from .base import FIXFieldBase
from .types import FIXPrice

class UnderlyingDirtyPrice(FIXFieldBase):
    """FIX UnderlyingDirtyPrice field."""
    tag: str = "882"
    name: str = "UnderlyingDirtyPrice"
    type: str = "PRICE"
    value: FIXPrice
