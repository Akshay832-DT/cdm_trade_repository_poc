
from .base import FIXFieldBase
from .types import FIXString

class SenderLocationID(FIXFieldBase):
    """FIX SenderLocationID field."""
    tag: str = "142"
    name: str = "SenderLocationID"
    type: str = "STRING"
    value: FIXString
