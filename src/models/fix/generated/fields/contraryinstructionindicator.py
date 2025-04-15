"""
FIX ContraryInstructionIndicator field (tag 719).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class ContraryInstructionIndicatorField(FIXFieldBase):
    """"""
    tag: str = "719"
    name: str = "ContraryInstructionIndicator"
    type: str = "BOOLEAN"
    value: bool
