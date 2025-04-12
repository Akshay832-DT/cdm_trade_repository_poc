
from .base import FIXFieldBase
from .types import FIXInt

class CustOrderCapacity(FIXFieldBase):
    """FIX CustOrderCapacity field."""
    tag: str = "582"
    name: str = "CustOrderCapacity"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 1: MEMBER_TRADING_FOR_THEIR_OWN_ACCOUNT
    # 2: CLEARING_FIRM_TRADING_FOR_ITS_PROPRIETARY_ACCOUNT
    # 3: MEMBER_TRADING_FOR_ANOTHER_MEMBER
    # 4: ALL_OTHER
