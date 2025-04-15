"""
FIX NoLegStipulations field (tag 683).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class NoLegStipulationsField(FIXFieldBase):
    """"""
    tag: str = "683"
    name: str = "NoLegStipulations"
    type: str = "NUMINGROUP"
    value: int
