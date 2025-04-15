"""
FIX Issuer field (tag 106).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class IssuerField(FIXFieldBase):
    """"""
    tag: str = "106"
    name: str = "Issuer"
    type: str = "STRING"
    value: str
