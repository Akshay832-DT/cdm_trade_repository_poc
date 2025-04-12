
from .base import FIXFieldBase
from .types import FIXChar

class SettlInstMode(FIXFieldBase):
    """FIX SettlInstMode field."""
    tag: str = "160"
    name: str = "SettlInstMode"
    type: str = "CHAR"
    value: FIXChar

    # Enum values
    # 1: STANDING_INSTRUCTIONS_PROVIDED
    # 4: SPECIFIC_ORDER_FOR_A_SINGLE_ACCOUNT
    # 5: REQUEST_REJECT
