
from .base import FIXFieldBase
from .types import FIXInt

class EventType(FIXFieldBase):
    """FIX EventType field."""
    tag: str = "865"
    name: str = "EventType"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 1: PUT
    # 2: CALL
    # 3: TENDER
    # 4: SINKING_FUND_CALL
    # 99: OTHER
