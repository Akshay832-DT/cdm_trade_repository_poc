
from .base import FIXFieldBase
from .types import FIXString

class ConfirmID(FIXFieldBase):
    """FIX ConfirmID field."""
    tag: str = "664"
    name: str = "ConfirmID"
    type: str = "STRING"
    value: FIXString
