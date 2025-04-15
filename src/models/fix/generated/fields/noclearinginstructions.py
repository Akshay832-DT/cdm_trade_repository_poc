"""
FIX NoClearingInstructions field (tag 576).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class NoClearingInstructionsField(FIXFieldBase):
    """"""
    tag: str = "576"
    name: str = "NoClearingInstructions"
    type: str = "NUMINGROUP"
    value: int
