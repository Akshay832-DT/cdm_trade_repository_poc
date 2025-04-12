
from .base import FIXFieldBase
from .types import FIXChar

class IOIQltyInd(FIXFieldBase):
    """FIX IOIQltyInd field."""
    tag: str = "25"
    name: str = "IOIQltyInd"
    type: str = "CHAR"
    value: FIXChar

    # Enum values
    # L: LOW
    # M: MEDIUM
    # H: HIGH
