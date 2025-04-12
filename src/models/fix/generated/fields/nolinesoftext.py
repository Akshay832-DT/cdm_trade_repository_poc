
from .base import FIXFieldBase
from .types import FIXNumInGroup

class NoLinesOfText(FIXFieldBase):
    """FIX NoLinesOfText field."""
    tag: str = "33"
    name: str = "NoLinesOfText"
    type: str = "NUMINGROUP"
    value: FIXNumInGroup
