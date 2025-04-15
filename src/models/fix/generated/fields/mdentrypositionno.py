"""
FIX MDEntryPositionNo field (tag 290).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class MDEntryPositionNoField(FIXFieldBase):
    """"""
    tag: str = "290"
    name: str = "MDEntryPositionNo"
    type: str = "INT"
    value: int
