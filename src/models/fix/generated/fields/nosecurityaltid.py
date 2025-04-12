
from .base import FIXFieldBase
from .types import FIXNumInGroup

class NoSecurityAltID(FIXFieldBase):
    """FIX NoSecurityAltID field."""
    tag: str = "454"
    name: str = "NoSecurityAltID"
    type: str = "NUMINGROUP"
    value: FIXNumInGroup
