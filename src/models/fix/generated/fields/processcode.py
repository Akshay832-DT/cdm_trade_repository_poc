
from .base import FIXFieldBase
from .types import FIXChar

class ProcessCode(FIXFieldBase):
    """FIX ProcessCode field."""
    tag: str = "81"
    name: str = "ProcessCode"
    type: str = "CHAR"
    value: FIXChar

    # Enum values
    # 0: REGULAR
    # 1: SOFT_DOLLAR
    # 2: STEP_IN
    # 3: STEP_OUT
    # 4: SOFT_DOLLAR_STEP_IN
    # 5: SOFT_DOLLAR_STEP_OUT
    # 6: PLAN_SPONSOR
