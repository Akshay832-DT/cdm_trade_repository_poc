
from .base import FIXFieldBase
from .types import FIXBoolean

class ReversalIndicator(FIXFieldBase):
    """FIX ReversalIndicator field."""
    tag: str = "700"
    name: str = "ReversalIndicator"
    type: str = "BOOLEAN"
    value: FIXBoolean
