
from .base import FIXFieldBase
from .types import FIXString

class TrdRegTimestampOrigin(FIXFieldBase):
    """FIX TrdRegTimestampOrigin field."""
    tag: str = "771"
    name: str = "TrdRegTimestampOrigin"
    type: str = "STRING"
    value: FIXString
