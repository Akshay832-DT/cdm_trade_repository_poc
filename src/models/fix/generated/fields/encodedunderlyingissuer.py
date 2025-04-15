"""
FIX EncodedUnderlyingIssuer field (tag 363).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class EncodedUnderlyingIssuerField(FIXFieldBase):
    """"""
    tag: str = "363"
    name: str = "EncodedUnderlyingIssuer"
    type: str = "DATA"
    value: str
