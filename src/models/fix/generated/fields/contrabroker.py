
from .base import FIXFieldBase
from .types import FIXString

class ContraBroker(FIXFieldBase):
    """FIX ContraBroker field."""
    tag: str = "375"
    name: str = "ContraBroker"
    type: str = "STRING"
    value: FIXString
