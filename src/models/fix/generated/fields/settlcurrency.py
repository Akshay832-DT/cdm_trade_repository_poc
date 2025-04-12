
from .base import FIXFieldBase
from .types import FIXCurrency

class SettlCurrency(FIXFieldBase):
    """FIX SettlCurrency field."""
    tag: str = "120"
    name: str = "SettlCurrency"
    type: str = "CURRENCY"
    value: FIXCurrency
