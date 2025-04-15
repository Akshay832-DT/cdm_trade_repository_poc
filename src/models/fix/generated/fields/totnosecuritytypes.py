"""
FIX TotNoSecurityTypes field (tag 557).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class TotNoSecurityTypesField(FIXFieldBase):
    """"""
    tag: str = "557"
    name: str = "TotNoSecurityTypes"
    type: str = "INT"
    value: int
