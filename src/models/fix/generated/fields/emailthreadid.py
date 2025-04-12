
from .base import FIXFieldBase
from .types import FIXString

class EmailThreadID(FIXFieldBase):
    """FIX EmailThreadID field."""
    tag: str = "164"
    name: str = "EmailThreadID"
    type: str = "STRING"
    value: FIXString
