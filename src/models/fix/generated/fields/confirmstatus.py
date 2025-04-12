
from .base import FIXFieldBase
from .types import FIXInt

class ConfirmStatus(FIXFieldBase):
    """FIX ConfirmStatus field."""
    tag: str = "665"
    name: str = "ConfirmStatus"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 1: RECEIVED
    # 2: MISMATCHED_ACCOUNT
    # 3: MISSING_SETTLEMENT_INSTRUCTIONS
    # 4: CONFIRMED
    # 5: REQUEST_REJECTED
