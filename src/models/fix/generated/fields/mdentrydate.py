
from .base import FIXFieldBase
from .types import FIXUTCDateOnly

class MDEntryDate(FIXFieldBase):
    """FIX MDEntryDate field."""
    tag: str = "272"
    name: str = "MDEntryDate"
    type: str = "UTCDATEONLY"
    value: FIXUTCDateOnly
