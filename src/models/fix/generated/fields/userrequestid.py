
from .base import FIXFieldBase
from .types import FIXString

class UserRequestID(FIXFieldBase):
    """FIX UserRequestID field."""
    tag: str = "923"
    name: str = "UserRequestID"
    type: str = "STRING"
    value: FIXString
