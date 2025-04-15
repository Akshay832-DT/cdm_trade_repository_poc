"""
FIX OrigPosReqRefID field (tag 713).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class OrigPosReqRefIDField(FIXFieldBase):
    """"""
    tag: str = "713"
    name: str = "OrigPosReqRefID"
    type: str = "STRING"
    value: str
