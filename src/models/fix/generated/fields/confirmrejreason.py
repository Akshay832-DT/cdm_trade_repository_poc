
from .base import FIXFieldBase
from .types import FIXInt

class ConfirmRejReason(FIXFieldBase):
    """FIX ConfirmRejReason field."""
    tag: str = "774"
    name: str = "ConfirmRejReason"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 1: MISMATCHED_ACCOUNT
    # 2: MISSING_SETTLEMENT_INSTRUCTIONS
    # 99: OTHER
