
from .base import FIXFieldBase
from .types import FIXInt

class CollInquiryResult(FIXFieldBase):
    """FIX CollInquiryResult field."""
    tag: str = "946"
    name: str = "CollInquiryResult"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 0: SUCCESSFUL
    # 1: INVALID_OR_UNKNOWN_INSTRUMENT
    # 2: INVALID_OR_UNKNOWN_COLLATERAL_TYPE
    # 3: INVALID_PARTIES
    # 4: INVALID_TRANSPORT_TYPE_REQUESTED
    # 5: INVALID_DESTINATION_REQUESTED
    # 6: NO_COLLATERAL_FOUND_FOR_THE_TRADE_SPECIFIED
    # 7: NO_COLLATERAL_FOUND_FOR_THE_ORDER_SPECIFIED
    # 8: COLLATERAL_INQUIRY_TYPE_NOT_SUPPORTED
    # 9: UNAUTHORIZED_FOR_COLLATERAL_INQUIRY
    # 99: OTHER
