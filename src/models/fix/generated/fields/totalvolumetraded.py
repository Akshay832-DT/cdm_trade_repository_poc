"""
FIX TotalVolumeTraded field (tag 387).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class TotalVolumeTradedField(FIXFieldBase):
    """"""
    tag: str = "387"
    name: str = "TotalVolumeTraded"
    type: str = "QTY"
    value: float
