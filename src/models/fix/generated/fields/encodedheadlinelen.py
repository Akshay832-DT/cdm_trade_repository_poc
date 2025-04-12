
from .base import FIXFieldBase
from .types import FIXLength

class EncodedHeadlineLen(FIXFieldBase):
    """FIX EncodedHeadlineLen field."""
    tag: str = "358"
    name: str = "EncodedHeadlineLen"
    type: str = "LENGTH"
    value: FIXLength
