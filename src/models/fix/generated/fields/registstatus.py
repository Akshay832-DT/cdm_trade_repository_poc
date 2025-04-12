
from .base import FIXFieldBase
from .types import FIXChar

class RegistStatus(FIXFieldBase):
    """FIX RegistStatus field."""
    tag: str = "506"
    name: str = "RegistStatus"
    type: str = "CHAR"
    value: FIXChar

    # Enum values
    # A: ACCEPTED
    # R: REJECTED
    # H: HELD
    # N: REMINDER
