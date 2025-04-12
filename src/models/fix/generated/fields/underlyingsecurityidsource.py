
from .base import FIXFieldBase
from .types import FIXString

class UnderlyingSecurityIDSource(FIXFieldBase):
    """FIX UnderlyingSecurityIDSource field."""
    tag: str = "305"
    name: str = "UnderlyingSecurityIDSource"
    type: str = "STRING"
    value: FIXString
