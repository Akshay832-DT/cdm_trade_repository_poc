
from .base import FIXFieldBase
from .types import FIXString

class LegStateOrProvinceOfIssue(FIXFieldBase):
    """FIX LegStateOrProvinceOfIssue field."""
    tag: str = "597"
    name: str = "LegStateOrProvinceOfIssue"
    type: str = "STRING"
    value: FIXString
