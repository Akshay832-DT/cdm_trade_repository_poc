
from .base import FIXFieldBase
from .types import FIXString

class LegCreditRating(FIXFieldBase):
    """FIX LegCreditRating field."""
    tag: str = "257"
    name: str = "LegCreditRating"
    type: str = "STRING"
    value: FIXString
