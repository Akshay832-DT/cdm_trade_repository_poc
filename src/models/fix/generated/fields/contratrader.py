
from .base import FIXFieldBase
from .types import FIXString

class ContraTrader(FIXFieldBase):
    """FIX ContraTrader field."""
    tag: str = "337"
    name: str = "ContraTrader"
    type: str = "STRING"
    value: FIXString
