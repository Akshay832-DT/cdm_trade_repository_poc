
from .base import FIXFieldBase
from .types import FIXChar

class DlvyInstType(FIXFieldBase):
    """FIX DlvyInstType field."""
    tag: str = "787"
    name: str = "DlvyInstType"
    type: str = "CHAR"
    value: FIXChar

    # Enum values
    # S: SECURITIES
    # C: CASH
