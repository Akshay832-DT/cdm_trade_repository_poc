
from .base import FIXFieldBase
from .types import FIXString

class Username(FIXFieldBase):
    """FIX Username field."""
    tag: str = "553"
    name: str = "Username"
    type: str = "STRING"
    value: FIXString
