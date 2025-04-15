"""
FIX EncodedLegIssuer field (tag 619).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class EncodedLegIssuerField(FIXFieldBase):
    """"""
    tag: str = "619"
    name: str = "EncodedLegIssuer"
    type: str = "DATA"
    value: str
