
from .base import FIXFieldBase
from .types import FIXString

class SecondaryOrderID(FIXFieldBase):
    """FIX SecondaryOrderID field."""
    tag: str = "198"
    name: str = "SecondaryOrderID"
    type: str = "STRING"
    value: FIXString
