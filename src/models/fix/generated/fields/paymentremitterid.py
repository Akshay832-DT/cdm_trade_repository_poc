
from .base import FIXFieldBase
from .types import FIXString

class PaymentRemitterID(FIXFieldBase):
    """FIX PaymentRemitterID field."""
    tag: str = "505"
    name: str = "PaymentRemitterID"
    type: str = "STRING"
    value: FIXString
