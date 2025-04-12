
from .base import FIXFieldBase
from .types import FIXCurrency

class Currency(FIXFieldBase):
    """FIX Currency field."""
    tag: str = "15"
    name: str = "Currency"
    type: str = "CURRENCY"
    value: FIXCurrency
