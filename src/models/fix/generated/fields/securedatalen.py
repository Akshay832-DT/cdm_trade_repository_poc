
from .base import FIXFieldBase
from .types import FIXLength

class SecureDataLen(FIXFieldBase):
    """FIX SecureDataLen field."""
    tag: str = "90"
    name: str = "SecureDataLen"
    type: str = "LENGTH"
    value: FIXLength
