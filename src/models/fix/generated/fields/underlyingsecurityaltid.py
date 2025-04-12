
from .base import FIXFieldBase
from .types import FIXString

class UnderlyingSecurityAltID(FIXFieldBase):
    """FIX UnderlyingSecurityAltID field."""
    tag: str = "458"
    name: str = "UnderlyingSecurityAltID"
    type: str = "STRING"
    value: FIXString
