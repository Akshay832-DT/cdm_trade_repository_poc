"""
FIX NoUnderlyingSecurityAltID field (tag 457).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class NoUnderlyingSecurityAltIDField(FIXFieldBase):
    """"""
    tag: str = "457"
    name: str = "NoUnderlyingSecurityAltID"
    type: str = "NUMINGROUP"
    value: int
