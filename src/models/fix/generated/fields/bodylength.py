
from .base import FIXFieldBase
from .types import FIXLength

class BodyLength(FIXFieldBase):
    """FIX BodyLength field."""
    tag: str = "9"
    name: str = "BodyLength"
    type: str = "LENGTH"
    value: FIXLength
