"""
FIX UnderlyingIssuer field (tag 306).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class UnderlyingIssuerField(FIXFieldBase):
    """"""
    tag: str = "306"
    name: str = "UnderlyingIssuer"
    type: str = "STRING"
    value: str
