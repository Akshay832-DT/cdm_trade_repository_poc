"""
FIX LegIssuer field (tag 617).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class LegIssuerField(FIXFieldBase):
    """"""
    tag: str = "617"
    name: str = "LegIssuer"
    type: str = "STRING"
    value: str
