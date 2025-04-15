"""
FIX EncodedUnderlyingSecurityDescLen field (tag 364).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class EncodedUnderlyingSecurityDescLenField(FIXFieldBase):
    """"""
    tag: str = "364"
    name: str = "EncodedUnderlyingSecurityDescLen"
    type: str = "LENGTH"
    value: int
