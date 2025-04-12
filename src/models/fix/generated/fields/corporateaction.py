
from .base import FIXFieldBase
from .types import FIXMultipleValueString

class CorporateAction(FIXFieldBase):
    """FIX CorporateAction field."""
    tag: str = "292"
    name: str = "CorporateAction"
    type: str = "MULTIPLEVALUESTRING"
    value: FIXMultipleValueString

    # Enum values
    # A: EX_DIVIDEND
    # B: EX_DISTRIBUTION
    # C: EX_RIGHTS
    # D: NEW
    # E: EX_INTEREST
