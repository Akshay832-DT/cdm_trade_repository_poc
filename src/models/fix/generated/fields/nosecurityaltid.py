"""
FIX NoSecurityAltID field (tag 454).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class NoSecurityAltIDField(FIXFieldBase):
    """"""
    tag: str = "454"
    name: str = "NoSecurityAltID"
    type: str = "NUMINGROUP"
    value: int
