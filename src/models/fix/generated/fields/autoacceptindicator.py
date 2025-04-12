
from .base import FIXFieldBase
from .types import FIXBoolean

class AutoAcceptIndicator(FIXFieldBase):
    """FIX AutoAcceptIndicator field."""
    tag: str = "754"
    name: str = "AutoAcceptIndicator"
    type: str = "BOOLEAN"
    value: FIXBoolean
