
from .base import FIXFieldBase
from .types import FIXNumInGroup

class NoQuoteEntries(FIXFieldBase):
    """FIX NoQuoteEntries field."""
    tag: str = "295"
    name: str = "NoQuoteEntries"
    type: str = "NUMINGROUP"
    value: FIXNumInGroup
