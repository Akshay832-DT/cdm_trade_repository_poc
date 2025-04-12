
from .base import FIXFieldBase
from .types import FIXChar

class UnderlyingOptAttribute(FIXFieldBase):
    """FIX UnderlyingOptAttribute field."""
    tag: str = "317"
    name: str = "UnderlyingOptAttribute"
    type: str = "CHAR"
    value: FIXChar
