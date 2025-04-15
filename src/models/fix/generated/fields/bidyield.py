"""
FIX BidYield field (tag 632).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class BidYieldField(FIXFieldBase):
    """"""
    tag: str = "632"
    name: str = "BidYield"
    type: str = "PERCENTAGE"
    value: float
