
from .base import FIXFieldBase
from .types import FIXString

class ComplianceID(FIXFieldBase):
    """FIX ComplianceID field."""
    tag: str = "376"
    name: str = "ComplianceID"
    type: str = "STRING"
    value: FIXString
