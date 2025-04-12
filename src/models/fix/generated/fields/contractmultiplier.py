
from .base import FIXFieldBase
from .types import FIXFloat

class ContractMultiplier(FIXFieldBase):
    """FIX ContractMultiplier field."""
    tag: str = "231"
    name: str = "ContractMultiplier"
    type: str = "FLOAT"
    value: FIXFloat
