
from .base import FIXFieldBase
from .types import FIXString

class AdvRefID(FIXFieldBase):
    """FIX AdvRefID field."""
    tag: str = "3"
    name: str = "AdvRefID"
    type: str = "STRING"
    value: FIXString
