
from .base import FIXFieldBase
from .types import FIXInt

class TotNumAssignmentReports(FIXFieldBase):
    """FIX TotNumAssignmentReports field."""
    tag: str = "832"
    name: str = "TotNumAssignmentReports"
    type: str = "INT"
    value: FIXInt
