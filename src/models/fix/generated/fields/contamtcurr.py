
from .base import FIXFieldBase
from .types import FIXCurrency

class ContAmtCurr(FIXFieldBase):
    """FIX ContAmtCurr field."""
    tag: str = "521"
    name: str = "ContAmtCurr"
    type: str = "CURRENCY"
    value: FIXCurrency
