
from .base import FIXFieldBase
from .types import FIXString

class Account(FIXFieldBase):
    """FIX Account field."""
    tag: str = "1"
    name: str = "Account"
    type: str = "STRING"
    value: FIXString
