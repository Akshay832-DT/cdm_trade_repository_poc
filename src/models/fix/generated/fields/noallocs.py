
from .base import FIXFieldBase
from .types import FIXNumInGroup

class NoAllocs(FIXFieldBase):
    """FIX NoAllocs field."""
    tag: str = "78"
    name: str = "NoAllocs"
    type: str = "NUMINGROUP"
    value: FIXNumInGroup
