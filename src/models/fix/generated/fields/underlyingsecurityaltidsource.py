"""
FIX UnderlyingSecurityAltIDSource field (tag 459).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class UnderlyingSecurityAltIDSourceField(FIXFieldBase):
    """"""
    tag: str = "459"
    name: str = "UnderlyingSecurityAltIDSource"
    type: str = "STRING"
    value: str
