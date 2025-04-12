
from .base import FIXFieldBase
from .types import FIXString

class TradeLegRefID(FIXFieldBase):
    """FIX TradeLegRefID field."""
    tag: str = "824"
    name: str = "TradeLegRefID"
    type: str = "STRING"
    value: FIXString
