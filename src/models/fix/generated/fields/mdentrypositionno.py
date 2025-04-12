
from .base import FIXFieldBase
from .types import FIXInt

class MDEntryPositionNo(FIXFieldBase):
    """FIX MDEntryPositionNo field."""
    tag: str = "290"
    name: str = "MDEntryPositionNo"
    type: str = "INT"
    value: FIXInt
