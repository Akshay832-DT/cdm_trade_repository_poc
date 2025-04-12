
from .base import FIXFieldBase
from .types import FIXString

class OnBehalfOfSubID(FIXFieldBase):
    """FIX OnBehalfOfSubID field."""
    tag: str = "116"
    name: str = "OnBehalfOfSubID"
    type: str = "STRING"
    value: FIXString
