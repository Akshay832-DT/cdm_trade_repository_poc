
from .base import FIXFieldBase
from .types import FIXLength

class EncodedSubjectLen(FIXFieldBase):
    """FIX EncodedSubjectLen field."""
    tag: str = "356"
    name: str = "EncodedSubjectLen"
    type: str = "LENGTH"
    value: FIXLength
