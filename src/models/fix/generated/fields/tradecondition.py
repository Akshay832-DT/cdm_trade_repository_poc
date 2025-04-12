
from .base import FIXFieldBase
from .types import FIXMultipleValueString

class TradeCondition(FIXFieldBase):
    """FIX TradeCondition field."""
    tag: str = "277"
    name: str = "TradeCondition"
    type: str = "MULTIPLEVALUESTRING"
    value: FIXMultipleValueString

    # Enum values
    # A: CASH
    # B: AVERAGE_PRICE_TRADE
    # C: CASH_TRADE
    # D: NEXT_DAY
    # E: OPENING
    # F: INTRADAY_TRADE_DETAIL
    # G: RULE127_TRADE
    # H: RULE155_TRADE
    # I: SOLD_LAST
    # J: NEXT_DAY_TRADE
    # K: OPENED
    # L: SELLER
    # M: SOLD
    # N: STOPPED_STOCK
    # P: IMBALANCE_MORE_BUYERS
    # Q: IMBALANCE_MORE_SELLERS
    # R: OPENING_PRICE
