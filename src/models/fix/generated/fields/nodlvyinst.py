"""
FIX NoDlvyInst field (tag 85).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class NoDlvyInstField(FIXFieldBase):
    """"""
    tag: str = "85"
    name: str = "NoDlvyInst"
    type: str = "NUMINGROUP"
    value: int
