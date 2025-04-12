
from .base import FIXFieldBase
from .types import FIXFloat

class UnderlyingContractMultiplier(FIXFieldBase):
    """FIX UnderlyingContractMultiplier field."""
    tag: str = "436"
    name: str = "UnderlyingContractMultiplier"
    type: str = "FLOAT"
    value: FIXFloat
