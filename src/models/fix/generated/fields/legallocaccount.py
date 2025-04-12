
from .base import FIXFieldBase
from .types import FIXString

class LegAllocAccount(FIXFieldBase):
    """FIX LegAllocAccount field."""
    tag: str = "671"
    name: str = "LegAllocAccount"
    type: str = "STRING"
    value: FIXString
