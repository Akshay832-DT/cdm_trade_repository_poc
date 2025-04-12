
from .base import FIXFieldBase
from .types import FIXChar

class ExecType(FIXFieldBase):
    """FIX ExecType field."""
    tag: str = "150"
    name: str = "ExecType"
    type: str = "CHAR"
    value: FIXChar

    # Enum values
    # 0: NEW
    # 3: DONE_FOR_DAY
    # 4: CANCELED
    # 5: REPLACED
    # 6: PENDING_CANCEL
    # 7: STOPPED
    # 8: REJECTED
    # 9: SUSPENDED
    # A: PENDING_NEW
    # B: CALCULATED
    # C: EXPIRED
    # D: RESTATED
    # E: PENDING_REPLACE
    # F: TRADE
    # G: TRADE_CORRECT
    # H: TRADE_CANCEL
    # I: ORDER_STATUS
