
from .base import FIXFieldBase
from .types import FIXString

class RFQReqID(FIXFieldBase):
    """FIX RFQReqID field."""
    tag: str = "644"
    name: str = "RFQReqID"
    type: str = "STRING"
    value: FIXString
