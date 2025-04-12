
from .base import FIXFieldBase
from .types import FIXString

class DeliverToSubID(FIXFieldBase):
    """FIX DeliverToSubID field."""
    tag: str = "129"
    name: str = "DeliverToSubID"
    type: str = "STRING"
    value: FIXString
