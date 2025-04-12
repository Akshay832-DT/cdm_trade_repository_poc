
from .base import FIXFieldBase
from .types import FIXInt

class RptSeq(FIXFieldBase):
    """FIX RptSeq field."""
    tag: str = "83"
    name: str = "RptSeq"
    type: str = "INT"
    value: FIXInt
