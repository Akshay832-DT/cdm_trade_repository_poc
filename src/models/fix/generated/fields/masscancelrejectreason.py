
from .base import FIXFieldBase
from .types import FIXChar

class MassCancelRejectReason(FIXFieldBase):
    """FIX MassCancelRejectReason field."""
    tag: str = "532"
    name: str = "MassCancelRejectReason"
    type: str = "CHAR"
    value: FIXChar

    # Enum values
    # 0: MASS_CANCEL_NOT_SUPPORTED
    # 1: INVALID_OR_UNKNOWN_SECURITY
    # 2: INVALID_OR_UNKOWN_UNDERLYING_SECURITY
    # 3: INVALID_OR_UNKNOWN_PRODUCT
    # 4: INVALID_OR_UNKNOWN_CFI_CODE
    # 5: INVALID_OR_UNKNOWN_SECURITY_TYPE
    # 6: INVALID_OR_UNKNOWN_TRADING_SESSION
    # 99: OTHER
