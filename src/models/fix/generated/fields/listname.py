
from .base import FIXFieldBase
from .types import FIXString

class ListName(FIXFieldBase):
    """FIX ListName field."""
    tag: str = "392"
    name: str = "ListName"
    type: str = "STRING"
    value: FIXString
