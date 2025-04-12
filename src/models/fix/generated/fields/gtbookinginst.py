
from .base import FIXFieldBase
from .types import FIXInt

class GTBookingInst(FIXFieldBase):
    """FIX GTBookingInst field."""
    tag: str = "427"
    name: str = "GTBookingInst"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 0: BOOK_OUT_ALL_TRADES_ON_DAY_OF_EXECUTION
    # 1: ACCUMULATE_UNTIL_FILLED_OR_EXPIRED
    # 2: ACCUMULATE_UNTIL_VERBALLLY_NOTIFIED_OTHERWISE
