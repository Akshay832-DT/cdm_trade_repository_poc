
from .base import FIXFieldBase
from .types import FIXNumInGroup

class NoRegistDtls(FIXFieldBase):
    """FIX NoRegistDtls field."""
    tag: str = "473"
    name: str = "NoRegistDtls"
    type: str = "NUMINGROUP"
    value: FIXNumInGroup
