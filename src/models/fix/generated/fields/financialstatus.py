
from .base import FIXFieldBase
from .types import FIXMultipleValueString

class FinancialStatus(FIXFieldBase):
    """FIX FinancialStatus field."""
    tag: str = "291"
    name: str = "FinancialStatus"
    type: str = "MULTIPLEVALUESTRING"
    value: FIXMultipleValueString

    # Enum values
    # 1: BANKRUPT
    # 2: PENDING_DELISTING
