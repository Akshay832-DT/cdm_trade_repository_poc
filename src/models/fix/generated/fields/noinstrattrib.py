
from .base import FIXFieldBase
from .types import FIXNumInGroup

class NoInstrAttrib(FIXFieldBase):
    """FIX NoInstrAttrib field."""
    tag: str = "870"
    name: str = "NoInstrAttrib"
    type: str = "NUMINGROUP"
    value: FIXNumInGroup
