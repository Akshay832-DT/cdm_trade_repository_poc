
from .base import FIXFieldBase
from .types import FIXString

class AllocID(FIXFieldBase):
    """FIX AllocID field."""
    tag: str = "70"
    name: str = "AllocID"
    type: str = "STRING"
    value: FIXString
