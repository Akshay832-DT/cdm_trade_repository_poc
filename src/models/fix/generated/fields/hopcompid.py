
from .base import FIXFieldBase
from .types import FIXString

class HopCompID(FIXFieldBase):
    """FIX HopCompID field."""
    tag: str = "628"
    name: str = "HopCompID"
    type: str = "STRING"
    value: FIXString
