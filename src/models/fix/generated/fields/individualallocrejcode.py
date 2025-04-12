
from .base import FIXFieldBase
from .types import FIXInt

class IndividualAllocRejCode(FIXFieldBase):
    """FIX IndividualAllocRejCode field."""
    tag: str = "776"
    name: str = "IndividualAllocRejCode"
    type: str = "INT"
    value: FIXInt
