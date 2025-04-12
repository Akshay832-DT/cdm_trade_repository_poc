
from .base import FIXFieldBase
from .types import FIXCurrency

class CashDistribCurr(FIXFieldBase):
    """FIX CashDistribCurr field."""
    tag: str = "478"
    name: str = "CashDistribCurr"
    type: str = "CURRENCY"
    value: FIXCurrency
