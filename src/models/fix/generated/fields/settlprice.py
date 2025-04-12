
from .base import FIXFieldBase
from .types import FIXPrice

class SettlPrice(FIXFieldBase):
    """FIX SettlPrice field."""
    tag: str = "730"
    name: str = "SettlPrice"
    type: str = "PRICE"
    value: FIXPrice
