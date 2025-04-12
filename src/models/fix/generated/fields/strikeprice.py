
from .base import FIXFieldBase
from .types import FIXPrice

class StrikePrice(FIXFieldBase):
    """FIX StrikePrice field."""
    tag: str = "202"
    name: str = "StrikePrice"
    type: str = "PRICE"
    value: FIXPrice
