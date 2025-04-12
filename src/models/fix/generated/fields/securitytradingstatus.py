
from .base import FIXFieldBase
from .types import FIXInt

class SecurityTradingStatus(FIXFieldBase):
    """FIX SecurityTradingStatus field."""
    tag: str = "326"
    name: str = "SecurityTradingStatus"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 1: OPENING_DELAY
    # 2: TRADING_HALT
    # 3: RESUME
    # 4: NO_OPEN
    # 5: PRICE_INDICATION
    # 6: TRADING_RANGE_INDICATION
    # 7: MARKET_IMBALANCE_BUY
    # 8: MARKET_IMBALANCE_SELL
    # 9: MARKET_ON_CLOSE_IMBALANCE_BUY
    # 10: MARKET_ON_CLOSE_IMBALANCE_SELL
    # 12: NO_MARKET_IMBALANCE
    # 13: NO_MARKET_ON_CLOSE_IMBALANCE
    # 14: ITS_PRE_OPENING
    # 15: NEW_PRICE_INDICATION
    # 16: TRADE_DISSEMINATION_TIME
    # 17: READY_TO_TRADE
    # 18: NOT_AVAILABLE_FOR_TRADING
    # 19: NOT_TRADED_ON_THIS_MARKET
    # 20: UNKNOWN_OR_INVALID
    # 21: PRE_OPEN
    # 22: OPENING_ROTATION
    # 23: FAST_MARKET
