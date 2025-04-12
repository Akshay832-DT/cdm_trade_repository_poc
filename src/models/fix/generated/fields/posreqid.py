
from .base import FIXFieldBase
from .types import FIXString

class PosReqID(FIXFieldBase):
    """FIX PosReqID field."""
    tag: str = "710"
    name: str = "PosReqID"
    type: str = "STRING"
    value: FIXString
