
from .base import FIXFieldBase
from .types import FIXString

class RefAllocID(FIXFieldBase):
    """FIX RefAllocID field."""
    tag: str = "72"
    name: str = "RefAllocID"
    type: str = "STRING"
    value: FIXString
