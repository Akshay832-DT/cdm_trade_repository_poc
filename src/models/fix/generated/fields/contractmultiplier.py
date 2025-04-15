"""
FIX ContractMultiplier field (tag 231).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class ContractMultiplierField(FIXFieldBase):
    """"""
    tag: str = "231"
    name: str = "ContractMultiplier"
    type: str = "FLOAT"
    value: float
