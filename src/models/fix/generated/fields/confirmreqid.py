
from .base import FIXFieldBase
from .types import FIXString

class ConfirmReqID(FIXFieldBase):
    """FIX ConfirmReqID field."""
    tag: str = "859"
    name: str = "ConfirmReqID"
    type: str = "STRING"
    value: FIXString
