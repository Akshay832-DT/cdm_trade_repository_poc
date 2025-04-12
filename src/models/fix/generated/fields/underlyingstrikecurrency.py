
from .base import FIXFieldBase
from .types import FIXCurrency

class UnderlyingStrikeCurrency(FIXFieldBase):
    """FIX UnderlyingStrikeCurrency field."""
    tag: str = "941"
    name: str = "UnderlyingStrikeCurrency"
    type: str = "CURRENCY"
    value: FIXCurrency
