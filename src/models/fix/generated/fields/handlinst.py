
from .base import FIXFieldBase
from .types import FIXChar

class HandlInst(FIXFieldBase):
    """FIX HandlInst field."""
    tag: str = "21"
    name: str = "HandlInst"
    type: str = "CHAR"
    value: FIXChar

    # Enum values
    # 1: AUTOMATED_EXECUTION_NO_INTERVENTION
    # 2: AUTOMATED_EXECUTION_INTERVENTION_OK
    # 3: MANUAL_ORDER
