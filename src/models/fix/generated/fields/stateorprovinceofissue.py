
from .base import FIXFieldBase
from .types import FIXString

class StateOrProvinceOfIssue(FIXFieldBase):
    """FIX StateOrProvinceOfIssue field."""
    tag: str = "471"
    name: str = "StateOrProvinceOfIssue"
    type: str = "STRING"
    value: FIXString
