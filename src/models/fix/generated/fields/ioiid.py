
from .base import FIXFieldBase
from .types import FIXString

class IOIID(FIXFieldBase):
    """FIX IOIID field."""
    tag: str = "23"
    name: str = "IOIID"
    type: str = "STRING"
    value: FIXString
