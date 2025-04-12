
from .base import FIXFieldBase
from .types import FIXString

class SecurityReqID(FIXFieldBase):
    """FIX SecurityReqID field."""
    tag: str = "320"
    name: str = "SecurityReqID"
    type: str = "STRING"
    value: FIXString
