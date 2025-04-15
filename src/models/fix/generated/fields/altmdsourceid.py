"""
FIX AltMDSourceID field (tag 817).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class AltMDSourceIDField(FIXFieldBase):
    """"""
    tag: str = "817"
    name: str = "AltMDSourceID"
    type: str = "STRING"
    value: str
