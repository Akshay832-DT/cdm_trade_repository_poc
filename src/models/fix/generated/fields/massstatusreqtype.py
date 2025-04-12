
from .base import FIXFieldBase
from .types import FIXInt

class MassStatusReqType(FIXFieldBase):
    """FIX MassStatusReqType field."""
    tag: str = "585"
    name: str = "MassStatusReqType"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 1: STATUS_FOR_ORDERS_FOR_A_SECURITY
    # 2: STATUS_FOR_ORDERS_FOR_AN_UNDERLYING_SECURITY
    # 3: STATUS_FOR_ORDERS_FOR_A_PRODUCT
    # 4: STATUS_FOR_ORDERS_FOR_ACFI_CODE
    # 5: STATUS_FOR_ORDERS_FOR_A_SECURITY_TYPE
    # 6: STATUS_FOR_ORDERS_FOR_A_TRADING_SESSION
    # 7: STATUS_FOR_ALL_ORDERS
    # 8: STATUS_FOR_ORDERS_FOR_A_PARTY_ID
