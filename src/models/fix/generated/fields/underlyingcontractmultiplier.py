"""
FIX UnderlyingContractMultiplier field (tag 436).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class UnderlyingContractMultiplierField(FIXFieldBase):
    """"""
    tag: str = "436"
    name: str = "UnderlyingContractMultiplier"
    type: str = "FLOAT"
    value: float
