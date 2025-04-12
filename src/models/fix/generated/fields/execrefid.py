
from .base import FIXFieldBase
from .types import FIXString

class ExecRefID(FIXFieldBase):
    """FIX ExecRefID field."""
    tag: str = "19"
    name: str = "ExecRefID"
    type: str = "STRING"
    value: FIXString
