
from .base import FIXFieldBase
from .types import FIXPrice

class PriorSettlPrice(FIXFieldBase):
    """FIX PriorSettlPrice field."""
    tag: str = "734"
    name: str = "PriorSettlPrice"
    type: str = "PRICE"
    value: FIXPrice
