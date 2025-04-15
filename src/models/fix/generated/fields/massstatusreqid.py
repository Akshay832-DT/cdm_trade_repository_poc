"""
FIX MassStatusReqID field (tag 584).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class MassStatusReqIDField(FIXFieldBase):
    """"""
    tag: str = "584"
    name: str = "MassStatusReqID"
    type: str = "STRING"
    value: str
