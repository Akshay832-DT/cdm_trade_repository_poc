
from .base import FIXFieldBase
from .types import FIXChar

class BidTradeType(FIXFieldBase):
    """FIX BidTradeType field."""
    tag: str = "418"
    name: str = "BidTradeType"
    type: str = "CHAR"
    value: FIXChar

    # Enum values
    # R: RISK_TRADE
    # G: VWAP_GUARANTEE
    # A: AGENCY
    # J: GUARANTEED_CLOSE
