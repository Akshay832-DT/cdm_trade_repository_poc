"""
FIX RoundingModulus field (tag 469).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class RoundingModulusField(FIXFieldBase):
    """"""
    tag: str = "469"
    name: str = "RoundingModulus"
    type: str = "FLOAT"
    value: float
