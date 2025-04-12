
from .base import FIXFieldBase
from .types import FIXNumInGroup

class NoClearingInstructions(FIXFieldBase):
    """FIX NoClearingInstructions field."""
    tag: str = "576"
    name: str = "NoClearingInstructions"
    type: str = "NUMINGROUP"
    value: FIXNumInGroup
