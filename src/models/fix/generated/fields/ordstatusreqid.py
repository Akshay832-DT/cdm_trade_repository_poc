
from .base import FIXFieldBase
from .types import FIXString

class OrdStatusReqID(FIXFieldBase):
    """FIX OrdStatusReqID field."""
    tag: str = "790"
    name: str = "OrdStatusReqID"
    type: str = "STRING"
    value: FIXString
