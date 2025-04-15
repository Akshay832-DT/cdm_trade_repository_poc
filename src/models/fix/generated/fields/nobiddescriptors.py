"""
FIX NoBidDescriptors field (tag 398).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class NoBidDescriptorsField(FIXFieldBase):
    """"""
    tag: str = "398"
    name: str = "NoBidDescriptors"
    type: str = "NUMINGROUP"
    value: int
