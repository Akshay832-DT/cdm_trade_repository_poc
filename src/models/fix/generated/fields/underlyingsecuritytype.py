
from .base import FIXFieldBase
from .types import FIXString

class UnderlyingSecurityType(FIXFieldBase):
    """FIX UnderlyingSecurityType field."""
    tag: str = "310"
    name: str = "UnderlyingSecurityType"
    type: str = "STRING"
    value: FIXString
