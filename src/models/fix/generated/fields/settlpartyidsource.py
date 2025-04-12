
from .base import FIXFieldBase
from .types import FIXChar

class SettlPartyIDSource(FIXFieldBase):
    """FIX SettlPartyIDSource field."""
    tag: str = "783"
    name: str = "SettlPartyIDSource"
    type: str = "CHAR"
    value: FIXChar
