
from .base import FIXFieldBase
from .types import FIXChar

class DayBookingInst(FIXFieldBase):
    """FIX DayBookingInst field."""
    tag: str = "589"
    name: str = "DayBookingInst"
    type: str = "CHAR"
    value: FIXChar

    # Enum values
    # 0: AUTO
    # 1: SPEAK_WITH_ORDER_INITIATOR_BEFORE_BOOKING
    # 2: ACCUMULATE
