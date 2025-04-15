"""
FIX TrdSubType field (tag 829).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class TrdSubTypeField(FIXFieldBase):
    """"""
    tag: str = "829"
    name: str = "TrdSubType"
    type: str = "INT"
    value: int
