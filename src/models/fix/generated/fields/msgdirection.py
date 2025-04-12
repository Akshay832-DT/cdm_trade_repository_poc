
from .base import FIXFieldBase
from .types import FIXChar

class MsgDirection(FIXFieldBase):
    """FIX MsgDirection field."""
    tag: str = "385"
    name: str = "MsgDirection"
    type: str = "CHAR"
    value: FIXChar

    # Enum values
    # S: SEND
    # R: RECEIVE
