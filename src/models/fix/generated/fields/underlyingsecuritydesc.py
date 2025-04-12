
from .base import FIXFieldBase
from .types import FIXString

class UnderlyingSecurityDesc(FIXFieldBase):
    """FIX UnderlyingSecurityDesc field."""
    tag: str = "307"
    name: str = "UnderlyingSecurityDesc"
    type: str = "STRING"
    value: FIXString
