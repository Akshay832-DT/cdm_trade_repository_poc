"""
FIX EncodedSecurityDescLen field (tag 350).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class EncodedSecurityDescLenField(FIXFieldBase):
    """"""
    tag: str = "350"
    name: str = "EncodedSecurityDescLen"
    type: str = "LENGTH"
    value: int
