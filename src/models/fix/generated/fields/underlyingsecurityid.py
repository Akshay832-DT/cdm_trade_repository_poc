
from .base import FIXFieldBase
from .types import FIXString

class UnderlyingSecurityID(FIXFieldBase):
    """FIX UnderlyingSecurityID field."""
    tag: str = "309"
    name: str = "UnderlyingSecurityID"
    type: str = "STRING"
    value: FIXString
