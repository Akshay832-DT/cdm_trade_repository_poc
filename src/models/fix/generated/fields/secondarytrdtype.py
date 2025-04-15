"""
FIX SecondaryTrdType field (tag 855).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class SecondaryTrdTypeField(FIXFieldBase):
    """"""
    tag: str = "855"
    name: str = "SecondaryTrdType"
    type: str = "INT"
    value: int
