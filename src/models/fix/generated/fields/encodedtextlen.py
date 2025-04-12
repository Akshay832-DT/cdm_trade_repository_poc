
from .base import FIXFieldBase
from .types import FIXLength

class EncodedTextLen(FIXFieldBase):
    """FIX EncodedTextLen field."""
    tag: str = "354"
    name: str = "EncodedTextLen"
    type: str = "LENGTH"
    value: FIXLength
