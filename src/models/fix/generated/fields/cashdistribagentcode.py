
from .base import FIXFieldBase
from .types import FIXString

class CashDistribAgentCode(FIXFieldBase):
    """FIX CashDistribAgentCode field."""
    tag: str = "499"
    name: str = "CashDistribAgentCode"
    type: str = "STRING"
    value: FIXString
