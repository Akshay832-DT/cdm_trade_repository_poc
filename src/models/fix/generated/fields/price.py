
from .base import FIXFieldBase
from .types import FIXPrice

class Price(FIXFieldBase):
    """FIX Price field."""
    tag: str = "44"
    name: str = "Price"
    type: str = "PRICE"
    value: FIXPrice
