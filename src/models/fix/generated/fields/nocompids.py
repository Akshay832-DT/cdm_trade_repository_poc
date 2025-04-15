"""
FIX NoCompIDs field (tag 936).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class NoCompIDsField(FIXFieldBase):
    """"""
    tag: str = "936"
    name: str = "NoCompIDs"
    type: str = "NUMINGROUP"
    value: int
