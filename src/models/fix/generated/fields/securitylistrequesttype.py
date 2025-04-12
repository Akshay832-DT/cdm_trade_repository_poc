
from .base import FIXFieldBase
from .types import FIXInt

class SecurityListRequestType(FIXFieldBase):
    """FIX SecurityListRequestType field."""
    tag: str = "559"
    name: str = "SecurityListRequestType"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 0: SYMBOL
    # 1: SECURITY_TYPE_AND
    # 2: PRODUCT
    # 3: TRADING_SESSION_ID
    # 4: ALL_SECURITIES
