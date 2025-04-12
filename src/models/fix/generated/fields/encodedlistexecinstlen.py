
from .base import FIXFieldBase
from .types import FIXLength

class EncodedListExecInstLen(FIXFieldBase):
    """FIX EncodedListExecInstLen field."""
    tag: str = "352"
    name: str = "EncodedListExecInstLen"
    type: str = "LENGTH"
    value: FIXLength
