
from .base import FIXFieldBase
from .types import FIXString

class AdvTransType(FIXFieldBase):
    """FIX AdvTransType field."""
    tag: str = "5"
    name: str = "AdvTransType"
    type: str = "STRING"
    value: FIXString

    # Enum values
    # N: NEW
    # C: CANCEL
    # R: REPLACE
