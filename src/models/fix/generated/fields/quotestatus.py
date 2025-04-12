
from .base import FIXFieldBase
from .types import FIXInt

class QuoteStatus(FIXFieldBase):
    """FIX QuoteStatus field."""
    tag: str = "297"
    name: str = "QuoteStatus"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 0: ACCEPTED
    # 1: CANCEL_FOR_SYMBOL
    # 2: CANCELED_FOR_SECURITY_TYPE
    # 3: CANCELED_FOR_UNDERLYING
    # 4: CANCELED_ALL
    # 5: REJECTED
    # 6: REMOVED_FROM_MARKET
    # 7: EXPIRED
    # 8: QUERY
    # 9: QUOTE_NOT_FOUND
    # 10: PENDING
    # 11: PASS
    # 12: LOCKED_MARKET_WARNING
    # 13: CROSS_MARKET_WARNING
    # 14: CANCELED_DUE_TO_LOCK_MARKET
    # 15: CANCELED_DUE_TO_CROSS_MARKET
