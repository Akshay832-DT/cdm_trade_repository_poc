
from .base import FIXFieldBase
from .types import FIXPrice

class LegPrice(FIXFieldBase):
    """FIX LegPrice field."""
    tag: str = "566"
    name: str = "LegPrice"
    type: str = "PRICE"
    value: FIXPrice
