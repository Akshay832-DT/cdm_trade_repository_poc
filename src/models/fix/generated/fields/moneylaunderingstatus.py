
from .base import FIXFieldBase
from .types import FIXChar

class MoneyLaunderingStatus(FIXFieldBase):
    """FIX MoneyLaunderingStatus field."""
    tag: str = "481"
    name: str = "MoneyLaunderingStatus"
    type: str = "CHAR"
    value: FIXChar

    # Enum values
    # Y: PASSED
    # N: NOT_CHECKED
    # 1: EXEMPT_BELOW_LIMIT
    # 2: EXEMPT_MONEY_TYPE
    # 3: EXEMPT_AUTHORISED
