
from .base import FIXFieldBase
from .types import FIXNumInGroup

class NoLegSecurityAltID(FIXFieldBase):
    """FIX NoLegSecurityAltID field."""
    tag: str = "604"
    name: str = "NoLegSecurityAltID"
    type: str = "NUMINGROUP"
    value: FIXNumInGroup
