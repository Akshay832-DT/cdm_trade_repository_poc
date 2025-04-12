
from .base import FIXFieldBase
from .types import FIXBoolean

class CopyMsgIndicator(FIXFieldBase):
    """FIX CopyMsgIndicator field."""
    tag: str = "797"
    name: str = "CopyMsgIndicator"
    type: str = "BOOLEAN"
    value: FIXBoolean
