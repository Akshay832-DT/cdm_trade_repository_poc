
from .base import FIXFieldBase
from .types import FIXPrice

class UnderlyingStrikePrice(FIXFieldBase):
    """FIX UnderlyingStrikePrice field."""
    tag: str = "316"
    name: str = "UnderlyingStrikePrice"
    type: str = "PRICE"
    value: FIXPrice
