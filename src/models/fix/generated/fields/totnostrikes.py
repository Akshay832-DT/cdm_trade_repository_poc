
from .base import FIXFieldBase
from .types import FIXInt

class TotNoStrikes(FIXFieldBase):
    """FIX TotNoStrikes field."""
    tag: str = "422"
    name: str = "TotNoStrikes"
    type: str = "INT"
    value: FIXInt
