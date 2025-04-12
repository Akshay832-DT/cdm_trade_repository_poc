
from .base import FIXFieldBase
from .types import FIXLength

class RawDataLength(FIXFieldBase):
    """FIX RawDataLength field."""
    tag: str = "95"
    name: str = "RawDataLength"
    type: str = "LENGTH"
    value: FIXLength
