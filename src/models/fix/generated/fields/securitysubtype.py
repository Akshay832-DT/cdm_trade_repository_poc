
from .base import FIXFieldBase
from .types import FIXString

class SecuritySubType(FIXFieldBase):
    """FIX SecuritySubType field."""
    tag: str = "762"
    name: str = "SecuritySubType"
    type: str = "STRING"
    value: FIXString
