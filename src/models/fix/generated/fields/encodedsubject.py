
from .base import FIXFieldBase
from .types import FIXData

class EncodedSubject(FIXFieldBase):
    """FIX EncodedSubject field."""
    tag: str = "357"
    name: str = "EncodedSubject"
    type: str = "DATA"
    value: FIXData
