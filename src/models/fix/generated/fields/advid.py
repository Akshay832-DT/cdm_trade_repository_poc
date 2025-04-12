
from .base import FIXFieldBase
from .types import FIXString

class AdvId(FIXFieldBase):
    """FIX AdvId field."""
    tag: str = "2"
    name: str = "AdvId"
    type: str = "STRING"
    value: FIXString
