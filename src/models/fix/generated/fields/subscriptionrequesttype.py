
from .base import FIXFieldBase
from .types import FIXChar

class SubscriptionRequestType(FIXFieldBase):
    """FIX SubscriptionRequestType field."""
    tag: str = "263"
    name: str = "SubscriptionRequestType"
    type: str = "CHAR"
    value: FIXChar

    # Enum values
    # 0: SNAPSHOT
    # 1: SNAPSHOT_AND_UPDATES
    # 2: DISABLE_PREVIOUS_SNAPSHOT
