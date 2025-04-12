
from .base import FIXFieldBase
from .types import FIXChar

class OptAttribute(FIXFieldBase):
    """FIX OptAttribute field."""
    tag: str = "206"
    name: str = "OptAttribute"
    type: str = "CHAR"
    value: FIXChar
