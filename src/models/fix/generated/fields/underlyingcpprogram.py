"""
FIX UnderlyingCPProgram field (tag 877).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class UnderlyingCPProgramField(FIXFieldBase):
    """"""
    tag: str = "877"
    name: str = "UnderlyingCPProgram"
    type: str = "STRING"
    value: str
