
from .base import FIXFieldBase
from .types import FIXChar

class QuoteQualifier(FIXFieldBase):
    """FIX QuoteQualifier field."""
    tag: str = "695"
    name: str = "QuoteQualifier"
    type: str = "CHAR"
    value: FIXChar
