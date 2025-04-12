
from .base import FIXFieldBase
from .types import FIXString

class UnderlyingCreditRating(FIXFieldBase):
    """FIX UnderlyingCreditRating field."""
    tag: str = "256"
    name: str = "UnderlyingCreditRating"
    type: str = "STRING"
    value: FIXString
