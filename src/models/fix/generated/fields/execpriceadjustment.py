"""
FIX ExecPriceAdjustment field (tag 485).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class ExecPriceAdjustmentField(FIXFieldBase):
    """"""
    tag: str = "485"
    name: str = "ExecPriceAdjustment"
    type: str = "FLOAT"
    value: float
