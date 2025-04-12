
from .base import FIXFieldBase
from .types import FIXString

class URLLink(FIXFieldBase):
    """FIX URLLink field."""
    tag: str = "149"
    name: str = "URLLink"
    type: str = "STRING"
    value: FIXString
