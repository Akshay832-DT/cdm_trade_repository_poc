
from .base import FIXFieldBase
from .types import FIXString

class SenderCompID(FIXFieldBase):
    """FIX SenderCompID field."""
    tag: str = "49"
    name: str = "SenderCompID"
    type: str = "STRING"
    value: FIXString
