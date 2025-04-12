
from .base import FIXFieldBase
from .types import FIXString

class UnderlyingCFICode(FIXFieldBase):
    """FIX UnderlyingCFICode field."""
    tag: str = "463"
    name: str = "UnderlyingCFICode"
    type: str = "STRING"
    value: FIXString
