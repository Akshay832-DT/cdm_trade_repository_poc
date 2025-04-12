
from .base import FIXFieldBase
from .types import FIXInt

class TotalNumPosReports(FIXFieldBase):
    """FIX TotalNumPosReports field."""
    tag: str = "727"
    name: str = "TotalNumPosReports"
    type: str = "INT"
    value: FIXInt
