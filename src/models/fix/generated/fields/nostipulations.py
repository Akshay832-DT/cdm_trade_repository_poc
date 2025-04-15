"""
FIX NoStipulations field (tag 232).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class NoStipulationsField(FIXFieldBase):
    """"""
    tag: str = "232"
    name: str = "NoStipulations"
    type: str = "NUMINGROUP"
    value: int
