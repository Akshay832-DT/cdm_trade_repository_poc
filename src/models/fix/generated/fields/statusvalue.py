
from .base import FIXFieldBase
from .types import FIXInt

class StatusValue(FIXFieldBase):
    """FIX StatusValue field."""
    tag: str = "928"
    name: str = "StatusValue"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 1: CONNECTED
    # 2: NOT_CONNECTED_UNEXPECTED
    # 3: NOT_CONNECTED_EXPECTED
    # 4: IN_PROCESS
