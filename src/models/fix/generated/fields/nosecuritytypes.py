"""
FIX NoSecurityTypes field (tag 558).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class NoSecurityTypesField(FIXFieldBase):
    """"""
    tag: str = "558"
    name: str = "NoSecurityTypes"
    type: str = "NUMINGROUP"
    value: int
