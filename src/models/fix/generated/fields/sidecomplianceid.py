
from .base import FIXFieldBase
from .types import FIXString

class SideComplianceID(FIXFieldBase):
    """FIX SideComplianceID field."""
    tag: str = "659"
    name: str = "SideComplianceID"
    type: str = "STRING"
    value: FIXString
