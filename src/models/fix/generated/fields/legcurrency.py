
from .base import FIXFieldBase
from .types import FIXCurrency

class LegCurrency(FIXFieldBase):
    """FIX LegCurrency field."""
    tag: str = "556"
    name: str = "LegCurrency"
    type: str = "CURRENCY"
    value: FIXCurrency
