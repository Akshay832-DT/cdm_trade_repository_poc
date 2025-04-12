
from .base import FIXFieldBase
from .types import FIXString

class OnBehalfOfLocationID(FIXFieldBase):
    """FIX OnBehalfOfLocationID field."""
    tag: str = "144"
    name: str = "OnBehalfOfLocationID"
    type: str = "STRING"
    value: FIXString
