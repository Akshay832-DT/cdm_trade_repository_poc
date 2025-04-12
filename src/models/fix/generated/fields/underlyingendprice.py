
from .base import FIXFieldBase
from .types import FIXPrice

class UnderlyingEndPrice(FIXFieldBase):
    """FIX UnderlyingEndPrice field."""
    tag: str = "883"
    name: str = "UnderlyingEndPrice"
    type: str = "PRICE"
    value: FIXPrice
