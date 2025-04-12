
from .base import FIXFieldBase
from .types import FIXString

class TradeReportRefID(FIXFieldBase):
    """FIX TradeReportRefID field."""
    tag: str = "572"
    name: str = "TradeReportRefID"
    type: str = "STRING"
    value: FIXString
