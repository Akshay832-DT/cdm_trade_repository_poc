
from .base import FIXFieldBase
from .types import FIXPrice

class ReportedPx(FIXFieldBase):
    """FIX ReportedPx field."""
    tag: str = "861"
    name: str = "ReportedPx"
    type: str = "PRICE"
    value: FIXPrice
