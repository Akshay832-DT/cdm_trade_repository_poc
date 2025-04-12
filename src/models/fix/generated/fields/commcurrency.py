
from .base import FIXFieldBase
from .types import FIXCurrency

class CommCurrency(FIXFieldBase):
    """FIX CommCurrency field."""
    tag: str = "479"
    name: str = "CommCurrency"
    type: str = "CURRENCY"
    value: FIXCurrency
