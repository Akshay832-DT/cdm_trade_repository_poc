
from .base import FIXFieldBase
from .types import FIXString

class RegistRefID(FIXFieldBase):
    """FIX RegistRefID field."""
    tag: str = "508"
    name: str = "RegistRefID"
    type: str = "STRING"
    value: FIXString
