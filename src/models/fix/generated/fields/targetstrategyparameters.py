"""
FIX TargetStrategyParameters field (tag 848).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class TargetStrategyParametersField(FIXFieldBase):
    """"""
    tag: str = "848"
    name: str = "TargetStrategyParameters"
    type: str = "STRING"
    value: str
