
from .base import FIXFieldBase
from .types import FIXNumInGroup

class NoQuoteQualifiers(FIXFieldBase):
    """FIX NoQuoteQualifiers field."""
    tag: str = "735"
    name: str = "NoQuoteQualifiers"
    type: str = "NUMINGROUP"
    value: FIXNumInGroup
