
from .base import FIXFieldBase
from .types import FIXString

class UserStatusText(FIXFieldBase):
    """FIX UserStatusText field."""
    tag: str = "927"
    name: str = "UserStatusText"
    type: str = "STRING"
    value: FIXString
