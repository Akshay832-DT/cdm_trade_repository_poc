
from .base import FIXFieldBase
from .types import FIXString

class MDReqID(FIXFieldBase):
    """FIX MDReqID field."""
    tag: str = "262"
    name: str = "MDReqID"
    type: str = "STRING"
    value: FIXString
