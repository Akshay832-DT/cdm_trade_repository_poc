
from .base import FIXFieldBase
from .types import FIXChar

class SettlInstTransType(FIXFieldBase):
    """FIX SettlInstTransType field."""
    tag: str = "163"
    name: str = "SettlInstTransType"
    type: str = "CHAR"
    value: FIXChar

    # Enum values
    # N: NEW
    # C: CANCEL
    # R: REPLACE
    # T: RESTATE
