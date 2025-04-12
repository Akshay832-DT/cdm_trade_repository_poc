
from .base import FIXFieldBase
from .types import FIXFloat

class LegContractMultiplier(FIXFieldBase):
    """FIX LegContractMultiplier field."""
    tag: str = "614"
    name: str = "LegContractMultiplier"
    type: str = "FLOAT"
    value: FIXFloat
