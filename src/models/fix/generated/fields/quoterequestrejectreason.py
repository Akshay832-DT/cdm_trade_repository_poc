
from .base import FIXFieldBase
from .types import FIXInt

class QuoteRequestRejectReason(FIXFieldBase):
    """FIX QuoteRequestRejectReason field."""
    tag: str = "658"
    name: str = "QuoteRequestRejectReason"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 1: UNKNOWN_SYMBOL
    # 2: EXCHANGE
    # 3: QUOTE_REQUEST_EXCEEDS_LIMIT
    # 4: TOO_LATE_TO_ENTER
    # 5: INVALID_PRICE
    # 6: NOT_AUTHORIZED_TO_REQUEST_QUOTE
    # 7: NO_MATCH_FOR_INQUIRY
    # 8: NO_MARKET_FOR_INSTRUMENT
    # 9: NO_INVENTORY
    # 10: PASS
    # 99: OTHER
