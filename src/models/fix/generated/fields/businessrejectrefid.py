
from .base import FIXFieldBase
from .types import FIXString

class BusinessRejectRefID(FIXFieldBase):
    """FIX BusinessRejectRefID field."""
    tag: str = "379"
    name: str = "BusinessRejectRefID"
    type: str = "STRING"
    value: FIXString
