
from .base import FIXFieldBase
from .types import FIXPrice

class UnderlyingSettlPrice(FIXFieldBase):
    """FIX UnderlyingSettlPrice field."""
    tag: str = "732"
    name: str = "UnderlyingSettlPrice"
    type: str = "PRICE"
    value: FIXPrice
