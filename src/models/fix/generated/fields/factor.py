"""
FIX Factor field (tag 228).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class FactorField(FIXFieldBase):
    """"""
    tag: str = "228"
    name: str = "Factor"
    type: str = "FLOAT"
    value: float
