
from .base import FIXFieldBase
from .types import FIXString

class SenderSubID(FIXFieldBase):
    """FIX SenderSubID field."""
    tag: str = "50"
    name: str = "SenderSubID"
    type: str = "STRING"
    value: FIXString
