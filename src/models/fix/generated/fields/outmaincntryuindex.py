
from .base import FIXFieldBase
from .types import FIXAmt

class OutMainCntryUIndex(FIXFieldBase):
    """FIX OutMainCntryUIndex field."""
    tag: str = "412"
    name: str = "OutMainCntryUIndex"
    type: str = "AMT"
    value: FIXAmt
