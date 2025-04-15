"""
FIX BuyVolume field (tag 330).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class BuyVolumeField(FIXFieldBase):
    """"""
    tag: str = "330"
    name: str = "BuyVolume"
    type: str = "QTY"
    value: float
