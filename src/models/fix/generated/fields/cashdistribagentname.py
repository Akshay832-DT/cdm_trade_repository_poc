
from .base import FIXFieldBase
from .types import FIXString

class CashDistribAgentName(FIXFieldBase):
    """FIX CashDistribAgentName field."""
    tag: str = "498"
    name: str = "CashDistribAgentName"
    type: str = "STRING"
    value: FIXString
