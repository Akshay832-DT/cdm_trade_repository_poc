
from .base import FIXFieldBase
from .types import FIXInt

class TotNumTradeReports(FIXFieldBase):
    """FIX TotNumTradeReports field."""
    tag: str = "748"
    name: str = "TotNumTradeReports"
    type: str = "INT"
    value: FIXInt
