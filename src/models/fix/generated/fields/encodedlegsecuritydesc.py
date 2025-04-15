"""
FIX EncodedLegSecurityDesc field (tag 622).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class EncodedLegSecurityDescField(FIXFieldBase):
    """"""
    tag: str = "622"
    name: str = "EncodedLegSecurityDesc"
    type: str = "DATA"
    value: str
