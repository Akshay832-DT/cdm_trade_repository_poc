
from .base import FIXFieldBase
from .types import FIXInt

class SettlPartySubIDType(FIXFieldBase):
    """FIX SettlPartySubIDType field."""
    tag: str = "786"
    name: str = "SettlPartySubIDType"
    type: str = "INT"
    value: FIXInt
