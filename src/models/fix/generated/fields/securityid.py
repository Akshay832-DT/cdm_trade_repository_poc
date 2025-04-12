
from .base import FIXFieldBase
from .types import FIXString

class SecurityID(FIXFieldBase):
    """FIX SecurityID field."""
    tag: str = "48"
    name: str = "SecurityID"
    type: str = "STRING"
    value: FIXString
