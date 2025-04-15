"""
FIX LegSecurityIDSource field (tag 603).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class LegSecurityIDSourceField(FIXFieldBase):
    """"""
    tag: str = "603"
    name: str = "LegSecurityIDSource"
    type: str = "STRING"
    value: str
