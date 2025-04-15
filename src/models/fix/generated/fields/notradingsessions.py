"""
FIX NoTradingSessions field (tag 386).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class NoTradingSessionsField(FIXFieldBase):
    """"""
    tag: str = "386"
    name: str = "NoTradingSessions"
    type: str = "NUMINGROUP"
    value: int
