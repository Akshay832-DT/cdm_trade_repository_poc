"""
FIX NoLegSecurityAltID field (tag 604).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class NoLegSecurityAltIDField(FIXFieldBase):
    """"""
    tag: str = "604"
    name: str = "NoLegSecurityAltID"
    type: str = "NUMINGROUP"
    value: int
