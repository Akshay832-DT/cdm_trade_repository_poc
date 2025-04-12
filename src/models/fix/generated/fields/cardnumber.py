
from .base import FIXFieldBase
from .types import FIXString

class CardNumber(FIXFieldBase):
    """FIX CardNumber field."""
    tag: str = "489"
    name: str = "CardNumber"
    type: str = "STRING"
    value: FIXString
