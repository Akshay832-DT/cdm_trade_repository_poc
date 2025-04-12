
from .base import FIXFieldBase
from .types import FIXString

class AllocAccount(FIXFieldBase):
    """FIX AllocAccount field."""
    tag: str = "79"
    name: str = "AllocAccount"
    type: str = "STRING"
    value: FIXString
