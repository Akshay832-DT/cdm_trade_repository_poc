
from .base import FIXFieldBase
from .types import FIXData

class EncodedAllocText(FIXFieldBase):
    """FIX EncodedAllocText field."""
    tag: str = "361"
    name: str = "EncodedAllocText"
    type: str = "DATA"
    value: FIXData
