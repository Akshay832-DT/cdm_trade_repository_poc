
from .base import FIXFieldBase
from .types import FIXString

class SecurityAltID(FIXFieldBase):
    """FIX SecurityAltID field."""
    tag: str = "455"
    name: str = "SecurityAltID"
    type: str = "STRING"
    value: FIXString
