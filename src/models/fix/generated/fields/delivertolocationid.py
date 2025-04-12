
from .base import FIXFieldBase
from .types import FIXString

class DeliverToLocationID(FIXFieldBase):
    """FIX DeliverToLocationID field."""
    tag: str = "145"
    name: str = "DeliverToLocationID"
    type: str = "STRING"
    value: FIXString
