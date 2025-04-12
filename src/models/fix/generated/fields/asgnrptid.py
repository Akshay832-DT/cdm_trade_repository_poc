
from .base import FIXFieldBase
from .types import FIXString

class AsgnRptID(FIXFieldBase):
    """FIX AsgnRptID field."""
    tag: str = "833"
    name: str = "AsgnRptID"
    type: str = "STRING"
    value: FIXString
