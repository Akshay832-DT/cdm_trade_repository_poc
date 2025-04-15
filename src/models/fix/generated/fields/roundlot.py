"""
FIX RoundLot field (tag 561).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class RoundLotField(FIXFieldBase):
    """"""
    tag: str = "561"
    name: str = "RoundLot"
    type: str = "QTY"
    value: float
