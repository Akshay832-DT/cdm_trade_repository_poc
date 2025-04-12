
from .base import FIXFieldBase
from .types import FIXInt

class TradeRequestResult(FIXFieldBase):
    """FIX TradeRequestResult field."""
    tag: str = "749"
    name: str = "TradeRequestResult"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 0: SUCCESSFUL
    # 1: INVALID_OR_UNKNOWN_INSTRUMENT
    # 2: INVALID_TYPE_OF_TRADE_REQUESTED
    # 3: INVALID_PARTIES
    # 4: INVALID_TRANSPORT_TYPE_REQUESTED
    # 5: INVALID_DESTINATION_REQUESTED
    # 8: TRADE_REQUEST_TYPE_NOT_SUPPORTED
    # 9: NOT_AUTHORIZED
    # 99: OTHER
