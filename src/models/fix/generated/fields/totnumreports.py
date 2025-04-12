
from .base import FIXFieldBase
from .types import FIXInt

class TotNumReports(FIXFieldBase):
    """FIX TotNumReports field."""
    tag: str = "911"
    name: str = "TotNumReports"
    type: str = "INT"
    value: FIXInt
