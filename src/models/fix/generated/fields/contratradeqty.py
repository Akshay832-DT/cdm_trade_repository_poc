
from .base import FIXFieldBase
from .types import FIXQty

class ContraTradeQty(FIXFieldBase):
    """FIX ContraTradeQty field."""
    tag: str = "437"
    name: str = "ContraTradeQty"
    type: str = "QTY"
    value: FIXQty
