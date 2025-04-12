
from .base import FIXFieldBase
from .types import FIXLength

class EncodedListStatusTextLen(FIXFieldBase):
    """FIX EncodedListStatusTextLen field."""
    tag: str = "445"
    name: str = "EncodedListStatusTextLen"
    type: str = "LENGTH"
    value: FIXLength
