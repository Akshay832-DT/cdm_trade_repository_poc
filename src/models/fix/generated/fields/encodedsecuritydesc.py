"""
FIX EncodedSecurityDesc field (tag 351).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class EncodedSecurityDescField(FIXFieldBase):
    """"""
    tag: str = "351"
    name: str = "EncodedSecurityDesc"
    type: str = "DATA"
    value: str
