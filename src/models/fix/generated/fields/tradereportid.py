
from .base import FIXFieldBase
from .types import FIXString

class TradeReportID(FIXFieldBase):
    """FIX TradeReportID field."""
    tag: str = "571"
    name: str = "TradeReportID"
    type: str = "STRING"
    value: FIXString
