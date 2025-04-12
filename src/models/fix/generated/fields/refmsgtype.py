
from .base import FIXFieldBase
from .types import FIXString

class RefMsgType(FIXFieldBase):
    """FIX RefMsgType field."""
    tag: str = "372"
    name: str = "RefMsgType"
    type: str = "STRING"
    value: FIXString
