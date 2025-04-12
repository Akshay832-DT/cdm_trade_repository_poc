
from .base import FIXFieldBase
from .types import FIXUTCTimestamp

class QuoteSetValidUntilTime(FIXFieldBase):
    """FIX QuoteSetValidUntilTime field."""
    tag: str = "367"
    name: str = "QuoteSetValidUntilTime"
    type: str = "UTCTIMESTAMP"
    value: FIXUTCTimestamp
