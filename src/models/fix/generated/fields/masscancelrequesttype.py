
from .base import FIXFieldBase
from .types import FIXChar

class MassCancelRequestType(FIXFieldBase):
    """FIX MassCancelRequestType field."""
    tag: str = "530"
    name: str = "MassCancelRequestType"
    type: str = "CHAR"
    value: FIXChar

    # Enum values
    # 1: CANCEL_ORDERS_FOR_A_SECURITY
    # 2: CANCEL_ORDERS_FOR_AN_UNDERLYING_SECURITY
    # 3: CANCEL_ORDERS_FOR_A_PRODUCT
    # 4: CANCEL_ORDERS_FOR_ACFI_CODE
    # 5: CANCEL_ORDERS_FOR_A_SECURITY_TYPE
    # 6: CANCEL_ORDERS_FOR_A_TRADING_SESSION
    # 7: CANCEL_ALL_ORDERS
