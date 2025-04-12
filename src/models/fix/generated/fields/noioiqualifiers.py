
from .base import FIXFieldBase
from .types import FIXNumInGroup

class NoIOIQualifiers(FIXFieldBase):
    """FIX NoIOIQualifiers field."""
    tag: str = "199"
    name: str = "NoIOIQualifiers"
    type: str = "NUMINGROUP"
    value: FIXNumInGroup
