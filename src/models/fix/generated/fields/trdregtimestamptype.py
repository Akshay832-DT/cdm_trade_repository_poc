
from .base import FIXFieldBase
from .types import FIXInt

class TrdRegTimestampType(FIXFieldBase):
    """FIX TrdRegTimestampType field."""
    tag: str = "770"
    name: str = "TrdRegTimestampType"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 1: EXECUTION_TIME
    # 2: TIME_IN
    # 3: TIME_OUT
    # 4: BROKER_RECEIPT
    # 5: BROKER_EXECUTION
