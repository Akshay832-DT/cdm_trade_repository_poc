
from .base import FIXFieldBase
from .types import FIXInt

class ApplQueueDepth(FIXFieldBase):
    """FIX ApplQueueDepth field."""
    tag: str = "813"
    name: str = "ApplQueueDepth"
    type: str = "INT"
    value: FIXInt
