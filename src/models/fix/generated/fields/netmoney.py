
from .base import FIXFieldBase
from .types import FIXAmt

class NetMoney(FIXFieldBase):
    """FIX NetMoney field."""
    tag: str = "118"
    name: str = "NetMoney"
    type: str = "AMT"
    value: FIXAmt
