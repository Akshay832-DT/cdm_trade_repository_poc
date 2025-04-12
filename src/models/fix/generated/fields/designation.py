
from .base import FIXFieldBase
from .types import FIXString

class Designation(FIXFieldBase):
    """FIX Designation field."""
    tag: str = "494"
    name: str = "Designation"
    type: str = "STRING"
    value: FIXString
