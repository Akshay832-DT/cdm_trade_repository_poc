"""
FIX PctAtRisk field (tag 869).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class PctAtRiskField(FIXFieldBase):
    """"""
    tag: str = "869"
    name: str = "PctAtRisk"
    type: str = "PERCENTAGE"
    value: float
