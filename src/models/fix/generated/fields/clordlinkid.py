
from .base import FIXFieldBase
from .types import FIXString

class ClOrdLinkID(FIXFieldBase):
    """FIX ClOrdLinkID field."""
    tag: str = "583"
    name: str = "ClOrdLinkID"
    type: str = "STRING"
    value: FIXString
