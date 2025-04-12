
from .base import FIXFieldBase
from .types import FIXNumInGroup

class NoMsgTypes(FIXFieldBase):
    """FIX NoMsgTypes field."""
    tag: str = "384"
    name: str = "NoMsgTypes"
    type: str = "NUMINGROUP"
    value: FIXNumInGroup
