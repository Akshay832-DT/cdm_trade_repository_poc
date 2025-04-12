
from .base import FIXFieldBase
from .types import FIXMonthYear

class LegContractSettlMonth(FIXFieldBase):
    """FIX LegContractSettlMonth field."""
    tag: str = "955"
    name: str = "LegContractSettlMonth"
    type: str = "MONTHYEAR"
    value: FIXMonthYear
