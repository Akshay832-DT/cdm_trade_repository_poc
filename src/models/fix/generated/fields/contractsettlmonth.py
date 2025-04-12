
from .base import FIXFieldBase
from .types import FIXMonthYear

class ContractSettlMonth(FIXFieldBase):
    """FIX ContractSettlMonth field."""
    tag: str = "667"
    name: str = "ContractSettlMonth"
    type: str = "MONTHYEAR"
    value: FIXMonthYear
