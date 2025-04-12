
from .base import FIXFieldBase
from .types import FIXPrice

class LegStrikePrice(FIXFieldBase):
    """FIX LegStrikePrice field."""
    tag: str = "612"
    name: str = "LegStrikePrice"
    type: str = "PRICE"
    value: FIXPrice
