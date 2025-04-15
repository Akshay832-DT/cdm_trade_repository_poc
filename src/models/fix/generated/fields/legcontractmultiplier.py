"""
FIX LegContractMultiplier field (tag 614).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class LegContractMultiplierField(FIXFieldBase):
    """"""
    tag: str = "614"
    name: str = "LegContractMultiplier"
    type: str = "FLOAT"
    value: float
