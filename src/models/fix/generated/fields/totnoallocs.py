
from .base import FIXFieldBase
from .types import FIXInt

class TotNoAllocs(FIXFieldBase):
    """FIX TotNoAllocs field."""
    tag: str = "892"
    name: str = "TotNoAllocs"
    type: str = "INT"
    value: FIXInt
