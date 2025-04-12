
from .base import FIXFieldBase
from .types import FIXInt

class TotNoQuoteEntries(FIXFieldBase):
    """FIX TotNoQuoteEntries field."""
    tag: str = "304"
    name: str = "TotNoQuoteEntries"
    type: str = "INT"
    value: FIXInt
