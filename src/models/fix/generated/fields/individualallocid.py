
from .base import FIXFieldBase
from .types import FIXString

class IndividualAllocID(FIXFieldBase):
    """FIX IndividualAllocID field."""
    tag: str = "467"
    name: str = "IndividualAllocID"
    type: str = "STRING"
    value: FIXString
