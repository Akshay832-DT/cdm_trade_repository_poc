"""
FIX EncodedIssuer field (tag 349).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class EncodedIssuerField(FIXFieldBase):
    """"""
    tag: str = "349"
    name: str = "EncodedIssuer"
    type: str = "DATA"
    value: str
