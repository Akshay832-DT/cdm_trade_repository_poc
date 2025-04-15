"""
FIX NoBidComponents field (tag 420).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class NoBidComponentsField(FIXFieldBase):
    """"""
    tag: str = "420"
    name: str = "NoBidComponents"
    type: str = "NUMINGROUP"
    value: int
