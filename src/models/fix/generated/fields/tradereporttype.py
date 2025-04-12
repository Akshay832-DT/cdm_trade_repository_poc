
from .base import FIXFieldBase
from .types import FIXInt

class TradeReportType(FIXFieldBase):
    """FIX TradeReportType field."""
    tag: str = "856"
    name: str = "TradeReportType"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 0: SUBMIT
    # 1: ALLEGED
    # 2: ACCEPT
    # 3: DECLINE
    # 4: ADDENDUM
    # 5: NO
    # 6: TRADE_REPORT_CANCEL
    # 7: LOCKED_IN
