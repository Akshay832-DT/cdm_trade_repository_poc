"""
FIX NoCapacities field (tag 862).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class NoCapacitiesField(FIXFieldBase):
    """"""
    tag: str = "862"
    name: str = "NoCapacities"
    type: str = "NUMINGROUP"
    value: int
