
from .base import FIXFieldBase
from .types import FIXCurrency

class AllowableOneSidednessCurr(FIXFieldBase):
    """FIX AllowableOneSidednessCurr field."""
    tag: str = "767"
    name: str = "AllowableOneSidednessCurr"
    type: str = "CURRENCY"
    value: FIXCurrency
