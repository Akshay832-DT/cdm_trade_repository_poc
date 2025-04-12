
from .base import FIXFieldBase
from .types import FIXString

class ConfirmRefID(FIXFieldBase):
    """FIX ConfirmRefID field."""
    tag: str = "772"
    name: str = "ConfirmRefID"
    type: str = "STRING"
    value: FIXString
