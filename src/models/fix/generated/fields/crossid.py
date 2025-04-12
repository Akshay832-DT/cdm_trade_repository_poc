
from .base import FIXFieldBase
from .types import FIXString

class CrossID(FIXFieldBase):
    """FIX CrossID field."""
    tag: str = "548"
    name: str = "CrossID"
    type: str = "STRING"
    value: FIXString
