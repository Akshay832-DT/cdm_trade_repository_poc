"""
FIX LegSecurityAltID field (tag 605).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class LegSecurityAltIDField(FIXFieldBase):
    """"""
    tag: str = "605"
    name: str = "LegSecurityAltID"
    type: str = "STRING"
    value: str
