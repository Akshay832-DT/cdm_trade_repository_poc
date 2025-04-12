
from .base import FIXFieldBase
from .types import FIXChar

class OrdStatus(FIXFieldBase):
    """FIX OrdStatus field."""
    tag: str = "39"
    name: str = "OrdStatus"
    type: str = "CHAR"
    value: FIXChar

    # Enum values
    # 0: NEW
    # 1: PARTIALLY_FILLED
    # 2: FILLED
    # 3: DONE_FOR_DAY
    # 4: CANCELED
    # 6: PENDING_CANCEL
    # 7: STOPPED
    # 8: REJECTED
    # 9: SUSPENDED
    # A: PENDING_NEW
    # B: CALCULATED
    # C: EXPIRED
    # D: ACCEPTED_FOR_BIDDING
    # E: PENDING_REPLACE
