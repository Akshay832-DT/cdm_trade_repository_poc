"""
FIX RFQReqID field (tag 644).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class RFQReqIDField(FIXFieldBase):
    """"""
    tag: str = "644"
    name: str = "RFQReqID"
    type: str = "STRING"
    value: str
