
from .base import FIXFieldBase
from .types import FIXLength

class EncodedAllocTextLen(FIXFieldBase):
    """FIX EncodedAllocTextLen field."""
    tag: str = "360"
    name: str = "EncodedAllocTextLen"
    type: str = "LENGTH"
    value: FIXLength
