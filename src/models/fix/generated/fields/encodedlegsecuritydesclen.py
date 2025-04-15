"""
FIX EncodedLegSecurityDescLen field (tag 621).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class EncodedLegSecurityDescLenField(FIXFieldBase):
    """"""
    tag: str = "621"
    name: str = "EncodedLegSecurityDescLen"
    type: str = "LENGTH"
    value: int
