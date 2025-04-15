"""
FIX EffectiveTime field (tag 168).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class EffectiveTimeField(FIXFieldBase):
    """"""
    tag: str = "168"
    name: str = "EffectiveTime"
    type: str = "UTCTIMESTAMP"
    value: datetime
