
from .base import FIXFieldBase
from .types import FIXString

class LocaleOfIssue(FIXFieldBase):
    """FIX LocaleOfIssue field."""
    tag: str = "472"
    name: str = "LocaleOfIssue"
    type: str = "STRING"
    value: FIXString
