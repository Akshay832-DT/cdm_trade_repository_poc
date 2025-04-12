
from .base import FIXFieldBase
from .types import FIXString

class RegistID(FIXFieldBase):
    """FIX RegistID field."""
    tag: str = "513"
    name: str = "RegistID"
    type: str = "STRING"
    value: FIXString
