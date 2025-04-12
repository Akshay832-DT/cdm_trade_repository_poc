
from .base import FIXFieldBase
from .types import FIXString

class UnderlyingCPProgram(FIXFieldBase):
    """FIX UnderlyingCPProgram field."""
    tag: str = "877"
    name: str = "UnderlyingCPProgram"
    type: str = "STRING"
    value: FIXString
