"""
FIX SellVolume field (tag 331).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class SellVolumeField(FIXFieldBase):
    """"""
    tag: str = "331"
    name: str = "SellVolume"
    type: str = "QTY"
    value: float
