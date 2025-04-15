"""
FIX NoDates field (tag 580).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class NoDatesField(FIXFieldBase):
    """"""
    tag: str = "580"
    name: str = "NoDates"
    type: str = "NUMINGROUP"
    value: int
