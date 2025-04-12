
from .base import FIXFieldBase
from .types import FIXCurrency

class StrikeCurrency(FIXFieldBase):
    """FIX StrikeCurrency field."""
    tag: str = "947"
    name: str = "StrikeCurrency"
    type: str = "CURRENCY"
    value: FIXCurrency
