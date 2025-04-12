
from .base import FIXFieldBase
from .types import FIXString

class Password(FIXFieldBase):
    """FIX Password field."""
    tag: str = "554"
    name: str = "Password"
    type: str = "STRING"
    value: FIXString
