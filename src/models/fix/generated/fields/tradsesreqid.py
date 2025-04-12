
from .base import FIXFieldBase
from .types import FIXString

class TradSesReqID(FIXFieldBase):
    """FIX TradSesReqID field."""
    tag: str = "335"
    name: str = "TradSesReqID"
    type: str = "STRING"
    value: FIXString
