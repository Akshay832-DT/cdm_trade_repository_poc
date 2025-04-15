"""
FIX EFPTrackingError field (tag 405).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class EFPTrackingErrorField(FIXFieldBase):
    """"""
    tag: str = "405"
    name: str = "EFPTrackingError"
    type: str = "PERCENTAGE"
    value: float
