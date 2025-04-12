
from .base import FIXFieldBase
from .types import FIXString

class CreditRating(FIXFieldBase):
    """FIX CreditRating field."""
    tag: str = "255"
    name: str = "CreditRating"
    type: str = "STRING"
    value: FIXString
