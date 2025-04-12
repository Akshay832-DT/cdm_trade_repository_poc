
from .base import FIXFieldBase
from .types import FIXString

class OrigPosReqRefID(FIXFieldBase):
    """FIX OrigPosReqRefID field."""
    tag: str = "713"
    name: str = "OrigPosReqRefID"
    type: str = "STRING"
    value: FIXString
