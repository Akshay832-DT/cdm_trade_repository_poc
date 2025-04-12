
from .base import FIXFieldBase
from .types import FIXString

class UnderlyingStateOrProvinceOfIssue(FIXFieldBase):
    """FIX UnderlyingStateOrProvinceOfIssue field."""
    tag: str = "593"
    name: str = "UnderlyingStateOrProvinceOfIssue"
    type: str = "STRING"
    value: FIXString
