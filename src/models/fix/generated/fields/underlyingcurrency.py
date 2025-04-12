
from .base import FIXFieldBase
from .types import FIXCurrency

class UnderlyingCurrency(FIXFieldBase):
    """FIX UnderlyingCurrency field."""
    tag: str = "318"
    name: str = "UnderlyingCurrency"
    type: str = "CURRENCY"
    value: FIXCurrency
