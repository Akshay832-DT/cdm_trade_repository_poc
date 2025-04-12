
from .base import FIXFieldBase
from .types import FIXInt

class QuoteEntryRejectReason(FIXFieldBase):
    """FIX QuoteEntryRejectReason field."""
    tag: str = "368"
    name: str = "QuoteEntryRejectReason"
    type: str = "INT"
    value: FIXInt
