
from .base import FIXFieldBase
from .types import FIXString

class SecurityAltIDSource(FIXFieldBase):
    """FIX SecurityAltIDSource field."""
    tag: str = "456"
    name: str = "SecurityAltIDSource"
    type: str = "STRING"
    value: FIXString
