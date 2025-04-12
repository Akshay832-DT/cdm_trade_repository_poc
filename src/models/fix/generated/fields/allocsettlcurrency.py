
from .base import FIXFieldBase
from .types import FIXCurrency

class AllocSettlCurrency(FIXFieldBase):
    """FIX AllocSettlCurrency field."""
    tag: str = "736"
    name: str = "AllocSettlCurrency"
    type: str = "CURRENCY"
    value: FIXCurrency
