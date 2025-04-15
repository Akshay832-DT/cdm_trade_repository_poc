"""
FIX NoUnderlyingStips field (tag 887).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class NoUnderlyingStipsField(FIXFieldBase):
    """"""
    tag: str = "887"
    name: str = "NoUnderlyingStips"
    type: str = "NUMINGROUP"
    value: int
