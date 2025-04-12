
from .base import FIXFieldBase
from .types import FIXString

class UnderlyingSecurityAltIDSource(FIXFieldBase):
    """FIX UnderlyingSecurityAltIDSource field."""
    tag: str = "459"
    name: str = "UnderlyingSecurityAltIDSource"
    type: str = "STRING"
    value: FIXString
