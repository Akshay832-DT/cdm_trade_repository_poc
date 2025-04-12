
from .base import FIXFieldBase
from .types import FIXString

class LegAllocAcctIDSource(FIXFieldBase):
    """FIX LegAllocAcctIDSource field."""
    tag: str = "674"
    name: str = "LegAllocAcctIDSource"
    type: str = "STRING"
    value: FIXString
