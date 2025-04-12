
from .base import FIXFieldBase
from .types import FIXInt

class QuoteRejectReason(FIXFieldBase):
    """FIX QuoteRejectReason field."""
    tag: str = "300"
    name: str = "QuoteRejectReason"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 1: UNKNOWN_SYMBOL
    # 2: EXCHANGE
    # 3: QUOTE_REQUEST_EXCEEDS_LIMIT
    # 4: TOO_LATE_TO_ENTER
    # 5: UNKNOWN_QUOTE
    # 6: DUPLICATE_QUOTE
    # 7: INVALID_BID
    # 8: INVALID_PRICE
    # 9: NOT_AUTHORIZED_TO_QUOTE_SECURITY
    # 99: OTHER
