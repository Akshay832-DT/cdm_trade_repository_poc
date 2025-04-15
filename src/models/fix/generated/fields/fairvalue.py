"""
FIX FairValue field (tag 406).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class FairValueField(FIXFieldBase):
    """"""
    tag: str = "406"
    name: str = "FairValue"
    type: str = "AMT"
    value: float
