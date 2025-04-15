"""
FIX BidID field (tag 390).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class BidIDField(FIXFieldBase):
    """"""
    tag: str = "390"
    name: str = "BidID"
    type: str = "STRING"
    value: str
