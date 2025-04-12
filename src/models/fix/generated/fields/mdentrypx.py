
from .base import FIXFieldBase
from .types import FIXPrice

class MDEntryPx(FIXFieldBase):
    """FIX MDEntryPx field."""
    tag: str = "270"
    name: str = "MDEntryPx"
    type: str = "PRICE"
    value: FIXPrice
