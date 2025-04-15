"""
FIX EncodedIssuerLen field (tag 348).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class EncodedIssuerLenField(FIXFieldBase):
    """"""
    tag: str = "348"
    name: str = "EncodedIssuerLen"
    type: str = "LENGTH"
    value: int
