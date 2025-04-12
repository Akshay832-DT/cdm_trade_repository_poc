
from .base import FIXFieldBase
from .types import FIXNumInGroup

class NoSecurityTypes(FIXFieldBase):
    """FIX NoSecurityTypes field."""
    tag: str = "558"
    name: str = "NoSecurityTypes"
    type: str = "NUMINGROUP"
    value: FIXNumInGroup
