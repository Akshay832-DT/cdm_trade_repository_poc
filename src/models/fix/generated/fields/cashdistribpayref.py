
from .base import FIXFieldBase
from .types import FIXString

class CashDistribPayRef(FIXFieldBase):
    """FIX CashDistribPayRef field."""
    tag: str = "501"
    name: str = "CashDistribPayRef"
    type: str = "STRING"
    value: FIXString
