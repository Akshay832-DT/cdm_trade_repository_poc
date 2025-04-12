
from .base import FIXFieldBase
from .types import FIXNumInGroup

class NoContraBrokers(FIXFieldBase):
    """FIX NoContraBrokers field."""
    tag: str = "382"
    name: str = "NoContraBrokers"
    type: str = "NUMINGROUP"
    value: FIXNumInGroup
