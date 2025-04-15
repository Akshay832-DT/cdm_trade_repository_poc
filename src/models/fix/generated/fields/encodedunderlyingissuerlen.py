"""
FIX EncodedUnderlyingIssuerLen field (tag 362).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class EncodedUnderlyingIssuerLenField(FIXFieldBase):
    """"""
    tag: str = "362"
    name: str = "EncodedUnderlyingIssuerLen"
    type: str = "LENGTH"
    value: int
