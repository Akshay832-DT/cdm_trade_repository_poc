
from .base import FIXFieldBase
from .types import FIXQty

class LegQty(FIXFieldBase):
    """FIX LegQty field."""
    tag: str = "687"
    name: str = "LegQty"
    type: str = "QTY"
    value: FIXQty
