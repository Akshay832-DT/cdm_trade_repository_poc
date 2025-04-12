
from .base import FIXFieldBase
from .types import FIXChar

class TimeInForce(FIXFieldBase):
    """FIX TimeInForce field."""
    tag: str = "59"
    name: str = "TimeInForce"
    type: str = "CHAR"
    value: FIXChar

    # Enum values
    # 0: DAY
    # 1: GOOD_TILL_CANCEL
    # 2: AT_THE_OPENING
    # 3: IMMEDIATE_OR_CANCEL
    # 4: FILL_OR_KILL
    # 5: GOOD_TILL_CROSSING
    # 6: GOOD_TILL_DATE
    # 7: AT_THE_CLOSE
