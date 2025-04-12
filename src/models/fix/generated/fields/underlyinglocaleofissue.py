
from .base import FIXFieldBase
from .types import FIXString

class UnderlyingLocaleOfIssue(FIXFieldBase):
    """FIX UnderlyingLocaleOfIssue field."""
    tag: str = "594"
    name: str = "UnderlyingLocaleOfIssue"
    type: str = "STRING"
    value: FIXString
