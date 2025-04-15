"""
FIX UnderlyingSecurityIDSource field (tag 305).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class UnderlyingSecurityIDSourceField(FIXFieldBase):
    """"""
    tag: str = "305"
    name: str = "UnderlyingSecurityIDSource"
    type: str = "STRING"
    value: str
