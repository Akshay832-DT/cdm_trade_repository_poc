
from .base import FIXFieldBase
from .types import FIXInt

class TradeReportRejectReason(FIXFieldBase):
    """FIX TradeReportRejectReason field."""
    tag: str = "751"
    name: str = "TradeReportRejectReason"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 0: SUCCESSFUL
    # 1: INVALID_PARTY_ONFORMATION
    # 2: UNKNOWN_INSTRUMENT
    # 3: UNAUTHORIZED_TO_REPORT_TRADES
    # 4: INVALID_TRADE_TYPE
    # 99: OTHER
