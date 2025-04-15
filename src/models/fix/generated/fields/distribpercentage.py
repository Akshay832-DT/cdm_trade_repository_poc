"""
FIX DistribPercentage field (tag 512).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class DistribPercentageField(FIXFieldBase):
    """"""
    tag: str = "512"
    name: str = "DistribPercentage"
    type: str = "PERCENTAGE"
    value: float
