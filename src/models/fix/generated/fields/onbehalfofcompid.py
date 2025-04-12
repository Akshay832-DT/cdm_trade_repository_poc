
from .base import FIXFieldBase
from .types import FIXString

class OnBehalfOfCompID(FIXFieldBase):
    """FIX OnBehalfOfCompID field."""
    tag: str = "115"
    name: str = "OnBehalfOfCompID"
    type: str = "STRING"
    value: FIXString
