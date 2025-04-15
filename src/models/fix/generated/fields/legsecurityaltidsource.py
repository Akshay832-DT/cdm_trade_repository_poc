"""
FIX LegSecurityAltIDSource field (tag 606).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class LegSecurityAltIDSourceField(FIXFieldBase):
    """"""
    tag: str = "606"
    name: str = "LegSecurityAltIDSource"
    type: str = "STRING"
    value: str
