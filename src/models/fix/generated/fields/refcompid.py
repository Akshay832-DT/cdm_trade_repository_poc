
from .base import FIXFieldBase
from .types import FIXString

class RefCompID(FIXFieldBase):
    """FIX RefCompID field."""
    tag: str = "930"
    name: str = "RefCompID"
    type: str = "STRING"
    value: FIXString
