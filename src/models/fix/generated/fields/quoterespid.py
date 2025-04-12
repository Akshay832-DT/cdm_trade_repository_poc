
from .base import FIXFieldBase
from .types import FIXString

class QuoteRespID(FIXFieldBase):
    """FIX QuoteRespID field."""
    tag: str = "693"
    name: str = "QuoteRespID"
    type: str = "STRING"
    value: FIXString
