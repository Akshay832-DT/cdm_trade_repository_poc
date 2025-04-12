
from .base import FIXFieldBase
from .types import FIXString

class CashDistribAgentAcctNumber(FIXFieldBase):
    """FIX CashDistribAgentAcctNumber field."""
    tag: str = "500"
    name: str = "CashDistribAgentAcctNumber"
    type: str = "STRING"
    value: FIXString
