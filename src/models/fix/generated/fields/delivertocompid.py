
from .base import FIXFieldBase
from .types import FIXString

class DeliverToCompID(FIXFieldBase):
    """FIX DeliverToCompID field."""
    tag: str = "128"
    name: str = "DeliverToCompID"
    type: str = "STRING"
    value: FIXString
