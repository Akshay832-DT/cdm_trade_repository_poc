"""
FIX HopRefID field (tag 630).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class HopRefIDField(FIXFieldBase):
    """"""
    tag: str = "630"
    name: str = "HopRefID"
    type: str = "SEQNUM"
    value: int
