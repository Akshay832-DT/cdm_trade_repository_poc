"""
FIX EncodedLegIssuerLen field (tag 618).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class EncodedLegIssuerLenField(FIXFieldBase):
    """"""
    tag: str = "618"
    name: str = "EncodedLegIssuerLen"
    type: str = "LENGTH"
    value: int
