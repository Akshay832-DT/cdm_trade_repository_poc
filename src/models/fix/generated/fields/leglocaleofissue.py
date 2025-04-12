
from .base import FIXFieldBase
from .types import FIXString

class LegLocaleOfIssue(FIXFieldBase):
    """FIX LegLocaleOfIssue field."""
    tag: str = "598"
    name: str = "LegLocaleOfIssue"
    type: str = "STRING"
    value: FIXString
