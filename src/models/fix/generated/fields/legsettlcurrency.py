
from .base import FIXFieldBase
from .types import FIXCurrency

class LegSettlCurrency(FIXFieldBase):
    """FIX LegSettlCurrency field."""
    tag: str = "675"
    name: str = "LegSettlCurrency"
    type: str = "CURRENCY"
    value: FIXCurrency
