
from .base import FIXFieldBase
from .types import FIXString

class ClientBidID(FIXFieldBase):
    """FIX ClientBidID field."""
    tag: str = "391"
    name: str = "ClientBidID"
    type: str = "STRING"
    value: FIXString
