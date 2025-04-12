
from .base import FIXFieldBase
from .types import FIXInt

class ApplQueueAction(FIXFieldBase):
    """FIX ApplQueueAction field."""
    tag: str = "815"
    name: str = "ApplQueueAction"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 0: NO_ACTION_TAKEN
    # 1: QUEUE_FLUSHED
    # 2: OVERLAY_LAST
    # 3: END_SESSION
