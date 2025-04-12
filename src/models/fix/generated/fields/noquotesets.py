
from .base import FIXFieldBase
from .types import FIXNumInGroup

class NoQuoteSets(FIXFieldBase):
    """FIX NoQuoteSets field."""
    tag: str = "296"
    name: str = "NoQuoteSets"
    type: str = "NUMINGROUP"
    value: FIXNumInGroup
