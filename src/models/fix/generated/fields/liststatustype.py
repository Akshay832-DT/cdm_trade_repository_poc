
from .base import FIXFieldBase
from .types import FIXInt

class ListStatusType(FIXFieldBase):
    """FIX ListStatusType field."""
    tag: str = "429"
    name: str = "ListStatusType"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 1: ACK
    # 2: RESPONSE
    # 3: TIMED
    # 4: EXEC_STARTED
    # 5: ALL_DONE
    # 6: ALERT
