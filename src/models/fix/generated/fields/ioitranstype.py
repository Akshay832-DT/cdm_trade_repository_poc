
from .base import FIXFieldBase
from .types import FIXChar

class IOITransType(FIXFieldBase):
    """FIX IOITransType field."""
    tag: str = "28"
    name: str = "IOITransType"
    type: str = "CHAR"
    value: FIXChar

    # Enum values
    # N: NEW
    # C: CANCEL
    # R: REPLACE
