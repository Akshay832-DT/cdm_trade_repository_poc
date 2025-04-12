
from .base import FIXFieldBase
from .types import FIXString

class SecurityDesc(FIXFieldBase):
    """FIX SecurityDesc field."""
    tag: str = "107"
    name: str = "SecurityDesc"
    type: str = "STRING"
    value: FIXString
