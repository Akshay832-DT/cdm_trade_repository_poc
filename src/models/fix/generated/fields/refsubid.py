
from .base import FIXFieldBase
from .types import FIXString

class RefSubID(FIXFieldBase):
    """FIX RefSubID field."""
    tag: str = "931"
    name: str = "RefSubID"
    type: str = "STRING"
    value: FIXString
