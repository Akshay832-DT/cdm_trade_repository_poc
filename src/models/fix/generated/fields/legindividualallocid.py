
from .base import FIXFieldBase
from .types import FIXString

class LegIndividualAllocID(FIXFieldBase):
    """FIX LegIndividualAllocID field."""
    tag: str = "672"
    name: str = "LegIndividualAllocID"
    type: str = "STRING"
    value: FIXString
