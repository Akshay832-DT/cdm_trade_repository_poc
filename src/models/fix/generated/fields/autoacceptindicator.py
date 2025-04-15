"""
FIX AutoAcceptIndicator field (tag 754).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class AutoAcceptIndicatorField(FIXFieldBase):
    """"""
    tag: str = "754"
    name: str = "AutoAcceptIndicator"
    type: str = "BOOLEAN"
    value: bool
