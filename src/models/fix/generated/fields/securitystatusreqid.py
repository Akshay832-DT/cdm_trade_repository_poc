
from .base import FIXFieldBase
from .types import FIXString

class SecurityStatusReqID(FIXFieldBase):
    """FIX SecurityStatusReqID field."""
    tag: str = "324"
    name: str = "SecurityStatusReqID"
    type: str = "STRING"
    value: FIXString
