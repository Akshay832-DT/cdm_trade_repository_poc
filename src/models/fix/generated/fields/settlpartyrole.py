
from .base import FIXFieldBase
from .types import FIXInt

class SettlPartyRole(FIXFieldBase):
    """FIX SettlPartyRole field."""
    tag: str = "784"
    name: str = "SettlPartyRole"
    type: str = "INT"
    value: FIXInt
