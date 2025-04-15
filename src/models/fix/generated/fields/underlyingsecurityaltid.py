"""
FIX UnderlyingSecurityAltID field (tag 458).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class UnderlyingSecurityAltIDField(FIXFieldBase):
    """"""
    tag: str = "458"
    name: str = "UnderlyingSecurityAltID"
    type: str = "STRING"
    value: str
