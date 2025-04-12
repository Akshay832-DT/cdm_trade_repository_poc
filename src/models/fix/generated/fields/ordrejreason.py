
from .base import FIXFieldBase
from .types import FIXInt

class OrdRejReason(FIXFieldBase):
    """FIX OrdRejReason field."""
    tag: str = "103"
    name: str = "OrdRejReason"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 0: BROKER_CREDIT
    # 1: UNKNOWN_SYMBOL
    # 2: EXCHANGE_CLOSED
    # 3: ORDER_EXCEEDS_LIMIT
    # 4: TOO_LATE_TO_ENTER
    # 5: UNKNOWN_ORDER
    # 6: DUPLICATE_ORDER
    # 7: DUPLICATE_OF_A_VERBALLY_COMMUNICATED_ORDER
    # 8: STALE_ORDER
    # 9: TRADE_ALONG_REQUIRED
    # 10: INVALID_INVESTOR_ID
    # 11: UNSUPPORTED_ORDER_CHARACTERISTIC
    # 13: INCORRECT_QUANTITY
    # 14: INCORRECT_ALLOCATED_QUANTITY
    # 15: UNKNOWN_ACCOUNT
    # 99: OTHER
