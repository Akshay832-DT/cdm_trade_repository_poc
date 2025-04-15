"""
FIX LegSecurityDesc field (tag 620).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class LegSecurityDescField(FIXFieldBase):
    """"""
    tag: str = "620"
    name: str = "LegSecurityDesc"
    type: str = "STRING"
    value: str
