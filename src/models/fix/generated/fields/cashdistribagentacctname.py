
from .base import FIXFieldBase
from .types import FIXString

class CashDistribAgentAcctName(FIXFieldBase):
    """FIX CashDistribAgentAcctName field."""
    tag: str = "502"
    name: str = "CashDistribAgentAcctName"
    type: str = "STRING"
    value: FIXString
