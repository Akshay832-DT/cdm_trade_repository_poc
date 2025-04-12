
from .base import FIXFieldBase
from .types import FIXCurrency

class MiscFeeCurr(FIXFieldBase):
    """FIX MiscFeeCurr field."""
    tag: str = "138"
    name: str = "MiscFeeCurr"
    type: str = "CURRENCY"
    value: FIXCurrency
