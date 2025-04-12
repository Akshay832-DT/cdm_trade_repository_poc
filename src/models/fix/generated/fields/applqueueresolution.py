
from .base import FIXFieldBase
from .types import FIXInt

class ApplQueueResolution(FIXFieldBase):
    """FIX ApplQueueResolution field."""
    tag: str = "814"
    name: str = "ApplQueueResolution"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 0: NO_ACTION_TAKEN
    # 1: QUEUE_FLUSHED
    # 2: OVERLAY_LAST
    # 3: END_SESSION
