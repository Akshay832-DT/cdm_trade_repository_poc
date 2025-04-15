"""
FIX TradeInputDevice field (tag 579).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class TradeInputDeviceField(FIXFieldBase):
    """"""
    tag: str = "579"
    name: str = "TradeInputDevice"
    type: str = "STRING"
    value: str
