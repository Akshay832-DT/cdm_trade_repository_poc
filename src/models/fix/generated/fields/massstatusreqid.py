
from .base import FIXFieldBase
from .types import FIXString

class MassStatusReqID(FIXFieldBase):
    """FIX MassStatusReqID field."""
    tag: str = "584"
    name: str = "MassStatusReqID"
    type: str = "STRING"
    value: FIXString
