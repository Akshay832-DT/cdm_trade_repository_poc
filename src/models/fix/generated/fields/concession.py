
from .base import FIXFieldBase
from .types import FIXAmt

class Concession(FIXFieldBase):
    """FIX Concession field."""
    tag: str = "238"
    name: str = "Concession"
    type: str = "AMT"
    value: FIXAmt
