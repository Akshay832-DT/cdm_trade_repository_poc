
from .base import FIXFieldBase
from .types import FIXString

class PaymentRef(FIXFieldBase):
    """FIX PaymentRef field."""
    tag: str = "476"
    name: str = "PaymentRef"
    type: str = "STRING"
    value: FIXString
