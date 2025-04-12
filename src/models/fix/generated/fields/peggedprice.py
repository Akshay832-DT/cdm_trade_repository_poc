
from .base import FIXFieldBase
from .types import FIXPrice

class PeggedPrice(FIXFieldBase):
    """FIX PeggedPrice field."""
    tag: str = "839"
    name: str = "PeggedPrice"
    type: str = "PRICE"
    value: FIXPrice
