
from .base import FIXFieldBase
from .types import FIXInt

class TotNoRelatedSym(FIXFieldBase):
    """FIX TotNoRelatedSym field."""
    tag: str = "393"
    name: str = "TotNoRelatedSym"
    type: str = "INT"
    value: FIXInt
