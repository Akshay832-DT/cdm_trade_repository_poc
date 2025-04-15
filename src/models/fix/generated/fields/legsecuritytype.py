"""
FIX LegSecurityType field (tag 609).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class LegSecurityTypeField(FIXFieldBase):
    """"""
    tag: str = "609"
    name: str = "LegSecurityType"
    type: str = "STRING"
    value: str
