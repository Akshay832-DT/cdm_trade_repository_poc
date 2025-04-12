
from .base import FIXFieldBase
from .types import FIXNumInGroup

class NoUnderlyingSecurityAltID(FIXFieldBase):
    """FIX NoUnderlyingSecurityAltID field."""
    tag: str = "457"
    name: str = "NoUnderlyingSecurityAltID"
    type: str = "NUMINGROUP"
    value: FIXNumInGroup
