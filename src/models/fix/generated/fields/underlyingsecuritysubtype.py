
from .base import FIXFieldBase
from .types import FIXString

class UnderlyingSecuritySubType(FIXFieldBase):
    """FIX UnderlyingSecuritySubType field."""
    tag: str = "763"
    name: str = "UnderlyingSecuritySubType"
    type: str = "STRING"
    value: FIXString
