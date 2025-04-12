
from .base import FIXFieldBase
from .types import FIXInt

class TradeReportTransType(FIXFieldBase):
    """FIX TradeReportTransType field."""
    tag: str = "487"
    name: str = "TradeReportTransType"
    type: str = "INT"
    value: FIXInt
