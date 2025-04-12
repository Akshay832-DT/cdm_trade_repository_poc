
from .base import FIXFieldBase
from .types import FIXInt

class ApplQueueMax(FIXFieldBase):
    """FIX ApplQueueMax field."""
    tag: str = "812"
    name: str = "ApplQueueMax"
    type: str = "INT"
    value: FIXInt
