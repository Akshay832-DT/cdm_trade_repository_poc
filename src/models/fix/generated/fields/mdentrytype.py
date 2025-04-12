
from .base import FIXFieldBase
from .types import FIXChar

class MDEntryType(FIXFieldBase):
    """FIX MDEntryType field."""
    tag: str = "269"
    name: str = "MDEntryType"
    type: str = "CHAR"
    value: FIXChar

    # Enum values
    # 0: BID
    # 1: OFFER
    # 2: TRADE
    # 3: INDEX_VALUE
    # 4: OPENING_PRICE
    # 5: CLOSING_PRICE
    # 6: SETTLEMENT_PRICE
    # 7: TRADING_SESSION_HIGH_PRICE
    # 8: TRADING_SESSION_LOW_PRICE
    # 9: TRADING_SESSION_VWAP_PRICE
    # A: IMBALANCE
    # B: TRADE_VOLUME
    # C: OPEN_INTEREST
