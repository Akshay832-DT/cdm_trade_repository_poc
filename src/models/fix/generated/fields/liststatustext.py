
from .base import FIXFieldBase
from .types import FIXString

class ListStatusText(FIXFieldBase):
    """FIX ListStatusText field."""
    tag: str = "444"
    name: str = "ListStatusText"
    type: str = "STRING"
    value: FIXString
