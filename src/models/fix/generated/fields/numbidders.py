"""
FIX NumBidders field (tag 417).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class NumBiddersField(FIXFieldBase):
    """"""
    tag: str = "417"
    name: str = "NumBidders"
    type: str = "INT"
    value: int
