
from .base import FIXFieldBase
from .types import FIXData

class EncodedHeadline(FIXFieldBase):
    """FIX EncodedHeadline field."""
    tag: str = "359"
    name: str = "EncodedHeadline"
    type: str = "DATA"
    value: FIXData
