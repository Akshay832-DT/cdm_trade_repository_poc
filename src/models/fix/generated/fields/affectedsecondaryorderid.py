
from .base import FIXFieldBase
from .types import FIXString

class AffectedSecondaryOrderID(FIXFieldBase):
    """FIX AffectedSecondaryOrderID field."""
    tag: str = "536"
    name: str = "AffectedSecondaryOrderID"
    type: str = "STRING"
    value: FIXString
