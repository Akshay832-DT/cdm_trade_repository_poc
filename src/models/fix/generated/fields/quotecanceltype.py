
from .base import FIXFieldBase
from .types import FIXInt

class QuoteCancelType(FIXFieldBase):
    """FIX QuoteCancelType field."""
    tag: str = "298"
    name: str = "QuoteCancelType"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 1: CANCEL_FOR_ONE_OR_MORE_SECURITIES
    # 2: CANCEL_FOR_SECURITY_TYPE
    # 3: CANCEL_FOR_UNDERLYING_SECURITY
    # 4: CANCEL_ALL_QUOTES
