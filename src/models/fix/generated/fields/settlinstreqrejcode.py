
from .base import FIXFieldBase
from .types import FIXInt

class SettlInstReqRejCode(FIXFieldBase):
    """FIX SettlInstReqRejCode field."""
    tag: str = "792"
    name: str = "SettlInstReqRejCode"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 0: UNABLE_TO_PROCESS_REQUEST
    # 1: UNKNOWN_ACCOUNT
    # 2: NO_MATCHING_SETTLEMENT_INSTRUCTIONS_FOUND
    # 99: OTHER
