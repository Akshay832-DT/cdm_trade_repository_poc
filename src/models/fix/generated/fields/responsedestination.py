
from .base import FIXFieldBase
from .types import FIXString

class ResponseDestination(FIXFieldBase):
    """FIX ResponseDestination field."""
    tag: str = "726"
    name: str = "ResponseDestination"
    type: str = "STRING"
    value: FIXString
