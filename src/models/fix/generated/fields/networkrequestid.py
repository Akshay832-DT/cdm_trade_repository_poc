
from .base import FIXFieldBase
from .types import FIXString

class NetworkRequestID(FIXFieldBase):
    """FIX NetworkRequestID field."""
    tag: str = "933"
    name: str = "NetworkRequestID"
    type: str = "STRING"
    value: FIXString
