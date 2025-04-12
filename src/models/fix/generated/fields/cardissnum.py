
from .base import FIXFieldBase
from .types import FIXString

class CardIssNum(FIXFieldBase):
    """FIX CardIssNum field."""
    tag: str = "491"
    name: str = "CardIssNum"
    type: str = "STRING"
    value: FIXString
