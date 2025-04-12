
from .base import FIXFieldBase
from .types import FIXString

class Text(FIXFieldBase):
    """FIX Text field."""
    tag: str = "58"
    name: str = "Text"
    type: str = "STRING"
    value: FIXString
