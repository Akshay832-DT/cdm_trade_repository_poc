
from .base import FIXFieldBase
from .types import FIXPrice

class DiscretionPrice(FIXFieldBase):
    """FIX DiscretionPrice field."""
    tag: str = "845"
    name: str = "DiscretionPrice"
    type: str = "PRICE"
    value: FIXPrice
